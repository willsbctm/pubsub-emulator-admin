import { Component, OnInit } from '@angular/core';
import { PubsubService } from '../pubsub.service';
import { GetTopicsResponse, Topic } from '@google-cloud/pubsub';

@Component({
  selector: 'app-topics',
  templateUrl: './topics.component.html',
  styleUrls: ['./topics.component.css']
})
export class TopicsComponent implements OnInit {
  topics: Topic[] = []; 

  constructor(private service: PubsubService) {
  }

  async ngOnInit(): Promise<void> {
    const response = await this.service.listAllTopics();
    if(response.length > 0){
      this.topics = response[0]
    }
  }

  async createTopic(name: string) {
    await this.service.createTopic(name);
  }
}
