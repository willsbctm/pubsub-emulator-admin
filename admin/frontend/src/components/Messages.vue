<script lang="ts">
import axios from 'axios'

export default {
  data() {
    return {
      topic: (this.$route.query["topic"] as string).split('/').slice(-1)[0],
      topicPath: this.$route.query["topic"],
      subscriptions: [] as string[]
    }
  },
  methods: {
    async sendMessage(){
      const message = (this.$refs.message as HTMLInputElement).value
      await axios.post(`http://localhost:8000/api/topics/${this.topic}/message`, message, { 
        headers: {
          'Content-Type': 'application/json'
        }
      });

      (this.$refs.message as HTMLInputElement).value = ''
    },
    async voltar(){
      this.$router.push({name: 'topics'})
    }
  }
}
</script>

<template>
  <main>
    <h1>{{ topicPath }}</h1>
    <h3>Message</h3>
    <div class="card">
      <div class="card-header">Name:</div>
      <div class="card-body">
        <div class="form-group">
          <textarea  ref="message" placeholder="Message" class="form-control" rows="40" cols="50"></textarea>
        </div>
        <button class="btn btn-sm btn-primary" id="message" @click="sendMessage()">Send</button>
      </div>
    </div>
    <button class="btn btn-sm btn-primary" @click="voltar">Voltar</button>
  </main>
</template>

<style>

</style>
