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
        <div class="col-md-12">
            <ul class="list-group">
                <li v-for="(topic, index) in topics" :key="index" ref="name" class="list-group-item">{{topic}}
                  <button class="btn btn-sm btn-primary" @click="sendMessage(topic)">Message</button>
                  <button class="btn btn-sm btn-primary" @click="getDetails(topic)">Details</button>
                  <button class="btn btn-sm btn-primary" @click="deleteTopic(topic)">Delete</button>
                </li>
                
            </ul>
        </div>
    </div>


    <div class="card">
      <div class="card-header">Name:</div>
      <div class="card-body">
        <div class="form-group">
          <input type="text" class="form-control" ref="name" placeholder="Name" />
        </div>
        <button class="btn btn-sm btn-primary" @click="createTopic">Create</button>
      </div>
    </div>
  </main>
</template>

<style>

</style>