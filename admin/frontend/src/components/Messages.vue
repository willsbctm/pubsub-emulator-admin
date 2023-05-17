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
    async back(){
      this.$router.push({name: 'topics'})
    }
  }
}
</script>

<template>
  <main>
  <div class="row">
    <div class="col-md-12">
        <h1>Message</h1>
        <h3>Topic: {{ topicPath }}</h3>
    </div>
  </div>

    <div class="row mb-5">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              {{ topic }}
            </div>
            <div class="card-body">
              <h5 class="card-title">Send message</h5>
                <textarea  ref="message" placeholder="{ 
  &quot;value&quot: 123
}" class="form-control" rows="30" cols="40"></textarea>
                <button type="button" class="btn btn-outline-primary me-1" @click="sendMessage">Send</button>
                <button type="button" class="btn btn-outline-secondary me-1" @click="back">Back</button>
            </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style>

</style>
