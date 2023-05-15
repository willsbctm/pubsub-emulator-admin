import { Component } from '@angular/core';
import { PubSub } from '@google-cloud/pubsub';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'pubsub-admin';
}
