<script lang="ts">
import axios from 'axios'

export default {
  data() {
    return {
      topics: [] as string[]
    }
  },
  methods: {
    async getTopics() {
      const topics = await axios.get<string[]>('http://localhost:8000/api/topics')
      this.topics = topics.data
    },
    async createTopic(){
      const name = (this.$refs.name as HTMLInputElement).value
      const data = {
        name: name
      }
      const topic = await axios.post('http://localhost:8000/api/topics', data)
      await this.getTopics();
      (this.$refs.name as HTMLInputElement).value = ''
    },
    async deleteTopic(topic: string){
      await axios.delete('http://localhost:8000/api/topics', {
        headers: {},
        data: {
          name: topic
        }
      })
      await this.getTopics()
    },
    async getDetails(topic: string){
      this.$router.push({ name: 'subscription', query: { topic: topic } })
    },
    async sendMessage(topic: string){
      this.$router.push({ name: 'message', query: { topic: topic } })
    },
    getName(topic: string) {
      return topic.split('/').slice(-1)[0]
    }
  },
  async mounted() {
    await this.getTopics()
  }
}
</script>


<template>
  <main>
    <div class="row">
      <div class="col-md-12">
          <h1>Topics</h1>
      </div>
    </div>

    <div class="row mb-5">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              Create topic
            </div>
            <div class="card-body">
              <h5 class="card-title">Name:</h5>
                <div class="mb-2">
                  <input type="text" class="form-control me-1" ref="name" placeholder="topic-payments" />
                </div>
              <button type="button" class="btn btn-outline-primary me-1" @click="createTopic">Create</button>
            </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-md-12">
          <h2>List:</h2>
      </div>
    </div>
    <div class="row">
        <div class="col-md-12">
          <div v-for="(topic, index) in topics" :key="index" class="card">
            <div class="card-header">
              - {{  topic }}
            </div>
            <div class="card-body">
              <h5 class="card-title">{{ getName(topic) }}</h5>
                <button type="button" class="btn btn-outline-secondary me-1" @click="sendMessage(topic)">Message</button>
                <button type="button" class="btn btn-outline-info me-1" @click="getDetails(topic)">Details</button>
                <button type="button" class="btn btn-outline-danger me-1" @click="deleteTopic(topic)">Delete</button>
            </div>
          </div>
        </div>
    </div>
  </main>
</template>

<style>

</style>