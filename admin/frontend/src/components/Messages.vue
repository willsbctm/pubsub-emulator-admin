<script lang="ts">
import axios from 'axios'

export default {
  data() {
    return {
      topic: (this.$route.query["topic"] as string).split('/').slice(-1)[0],
      topicPath: this.$route.query["topic"],
      subscriptions: [] as string[],
      message: ''
    }
  },
  methods: {
    async sendMessage(){
      const data = JSON.stringify(this.$refs.message.value)
      await axios.post(`http://localhost:8000/api/topics/${this.topic}/message`, data, { 
        headers: {
          'Content-Type': 'application/json'
        }
      })
      this.$refs.message.value = ''
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
          <input type="text" class="form-control" ref="message" placeholder="Message" />
        </div>
        <button class="btn btn-sm btn-primary" id="message" @click="sendMessage()">Send</button>
      </div>
    </div>
    <button class="btn btn-sm btn-primary" @click="voltar">Voltar</button>
  </main>
</template>

<style>

</style>
