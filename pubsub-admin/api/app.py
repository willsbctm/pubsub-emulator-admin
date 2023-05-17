from flask import Flask, jsonify
from google.cloud import pubsub_v1

project_id = 'test-project'
app = Flask("pubsub-admin-api")
project_path = f"projects/{project_id}"

@app.route('/topics', methods=['GET'])
def list_topics():
    publisher = pubsub_v1.PublisherClient()
    topics = publisher.list_topics(request={"project": project_path})
    jsonTopics = jsonify(topics)
    print(f"List topic: {jsonTopics}")
    return jsonTopics

@app.route('/teste', methods=['GET'])
def teste():
    return 'oi'

def create_app():
   return app