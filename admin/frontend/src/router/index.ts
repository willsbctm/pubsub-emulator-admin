import { createRouter, createWebHistory } from 'vue-router'
import Topics from '../components/Topics.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Topics
    },
    {
      path: '/topics',
      name: 'topics',
      component: Topics
    },
    {
      path: '/topics/subscription',
      name: 'subscription',
      component: () => import('../components/Subscriptions.vue')
    },
    {
      path: '/topics/message',
      name: 'message',
      component: () => import('../components/Messages.vue')
    }
  ]
})

export default router
