import json
from flask import Flask, jsonify, request
from google.cloud import pubsub_v1
from os import environ
from flask_cors import CORS

app = Flask("pubsub-admin-api")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

project_id = environ.get('PUBSUB_PROJECT_ID')

@app.route('/api/topics', methods=['GET'])
def list_topics():
    project_path = f"projects/{project_id}"
    publisher = pubsub_v1.PublisherClient()
    response = []
    for topic in publisher.list_topics(request={"project": project_path}):
        response.append(topic.name)
    return jsonify(response)

@app.route('/api/topics', methods=['POST'])
def create_topic():
    record = json.loads(request.data)
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, record["name"])
    topic = publisher.create_topic(request={"name": topic_path})
    return topic.name

@app.route('/api/topics', methods=['DELETE'])
def delete_topic():
    record = json.loads(request.data)
    topic_path = record["name"]
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()

    with subscriber:
        for subscription in publisher.list_topic_subscriptions(request={"topic": topic_path}):
            subscriber.delete_subscription(request={"subscription": subscription})

    publisher.delete_topic(request={"topic": topic_path})
    return record["name"]

@app.route('/api/topics/<topic>/subscriptions', methods=['POST'])
def create_topic_subscription(topic):
    record = json.loads(request.data)
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic)
    subscription_path = subscriber.subscription_path(project_id, record["name"])

    with subscriber:
        subscription = subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )
    return subscription.name

@app.route('/api/topics/<topic>/subscriptions', methods=['GET'])
def list_topic_subscriptions(topic):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic)
    response = []
    for subscription in publisher.list_topic_subscriptions(request={"topic": topic_path}):
        response.append(subscription)
    return jsonify(response)

@app.route('/api/topics/<topic>/message', methods=['POST'])
def send_message(topic):
    record = json.loads(request.data)
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic)

    data_str = json.dumps(record)
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_path, data)

    return future.result()

@app.route('/api/subscriptions', methods=['DELETE'])
def delete_subscription():
    record = json.loads(request.data)
    subscriber = pubsub_v1.SubscriberClient()
    with subscriber:
        subscriber.delete_subscription(request={"subscription": record["name"]})
    return record["name"]

@app.route('/api/subscriptions', methods=['GET'])
def list_subscriptions():
    subscriber = pubsub_v1.SubscriberClient()
    project_path = f"projects/{project_id}"
    response = []
    with subscriber:
        for subscription in subscriber.list_subscriptions(
            request={"project": project_path}
        ):
            response.append(subscription.name)
    return jsonify(response)



app.run(host='0.0.0.0', port=8000)
