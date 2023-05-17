import { Injectable } from '@angular/core';
import { CreateSubscriptionResponse, CreateTopicResponse, EmptyResponse, GetTopicSubscriptionsResponse, GetTopicsResponse, PubSub } from '@google-cloud/pubsub';

@Injectable({
  providedIn: 'root'
})

export class PubsubService {
  client: PubSub
  constructor() { 
    this.client = new PubSub({ apiEndpoint: "localhost", port: 8432 })
  }

  async listAllTopics(): Promise<GetTopicsResponse> {
    return await this.client.getTopics()
  }

  async listSubscriptions(topicNameOrId: string): Promise<GetTopicSubscriptionsResponse> {
    return await this.client.topic(topicNameOrId).getSubscriptions()
  }

  async createSubscription(topicNameOrId: string, subscriptionNameOrId: string): Promise<CreateSubscriptionResponse> {
    return await this.client
      .topic(topicNameOrId)
      .createSubscription(subscriptionNameOrId)
  }

  async createTopic(topicNameOrId: string):Promise<CreateTopicResponse> {
    return await this.client.createTopic(topicNameOrId)
  }

  async deleteTopic(topicNameOrId: string):Promise<EmptyResponse> {
    return await this.client.topic(topicNameOrId).delete()
  }

  async deleteSubscription(subscriptionNameOrId: string):Promise<EmptyResponse> {
    return await this.client.subscription(subscriptionNameOrId).delete()
  }

  async publishMessage(topicNameOrId: string, data: any): Promise<string> {
    const dataBuffer = Buffer.from(data);
    try {
      return await this.client
        .topic(topicNameOrId)
        .publishMessage({data: dataBuffer});
    } catch (error: any) {
      console.error(`Received error while publishing: ${error.message}`);
      process.exitCode = 1;
      return error.message;
    }
  }
}
