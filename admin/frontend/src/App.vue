<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-light bg-light mb-3">
  <a class="navbar-brand" href="/">
    <img src="@/assets/logo.svg" width="30" height="30" class="d-inline-block align-top" alt="">
      Pubsub Emulator Admin
  </a>
</nav>

  <RouterView />
</template>

<style scoped>

</style>
