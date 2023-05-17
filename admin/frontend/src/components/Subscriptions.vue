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
    async getSubscriptions() {
      const subscriptions = await axios.get<string[]>(`http://localhost:8000/api/topics/${this.topic}/subscriptions`)
      this.subscriptions = subscriptions.data
    },
    async createSubscription(){
      const name = (this.$refs.name as HTMLInputElement).value
      const data = {
        name: name
      }
      const topic = await axios.post(`http://localhost:8000/api/topics/${this.topic}/subscriptions`, data)
      await this.getSubscriptions();
      (this.$refs.name as HTMLInputElement).value = ''
    },
    async deleteSubscription(subscription: string){
      await axios.delete('http://localhost:8000/api/subscriptions', {
        headers: {},
        data: {
          name: subscription
        }
      })
      await this.getSubscriptions()
    },
    async back(){
      this.$router.push({name: 'topics'})
    }
  },
  async mounted() {
    await this.getSubscriptions()
  }
}
</script>


<template>
  <main>
  <div class="row">
    <div class="col-md-12">
        <h1>Subscriptions</h1>
        <h3>Topic: {{ topicPath }}</h3>
    </div>
  </div>

    <div class="row mb-5">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              Create Subscription
            </div>
            <div class="card-body">
              <h5 class="card-title">Name:</h5>
              <div class="mb-2">
                <input type="text" class="form-control me-1" ref="name" placeholder="sub-topic-payments" />
              </div>
                <button type="button" class="btn btn-outline-primary me-1"  @click="createSubscription">Create</button>
                <button type="button" class="btn btn-outline-secondary me-1" @click="back">Back</button>
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
          <div v-for="(sub, index) in subscriptions" :key="index" class="card">
            <div class="card-header">
              - {{  topic }}
            </div>
            <div class="card-body">
              <h5 class="card-title">{{ sub }}</h5>
                <button type="button" class="btn btn-outline-danger me-1" @click="deleteSubscription(sub)">Delete</button>
            </div>
          </div>
        </div>
    </div>
    </main>
</template>

<style>

</style>
