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
    async voltar(){
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
            <h1>{{ topicPath }}</h1>
            <h3>Subscriptions</h3>
        </div>
        <div class="col-md-12">
            <ul class="list-group">
                <li v-for="(sub, index) in subscriptions" :key="index" ref="name" class="list-group-item">{{sub}}
                  <button class="btn btn-sm btn-primary" @click="deleteSubscription(sub)">Delete</button>
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
        <button class="btn btn-sm btn-primary" @click="createSubscription">Create</button>
      </div>
    </div>
    <button class="btn btn-sm btn-primary" @click="voltar">Voltar</button>
  </main>
</template>

<style>

</style>
