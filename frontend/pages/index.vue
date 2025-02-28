<template>
    <div id="app">
      <h1>Welcome to the App</h1>
    </div>
</template>
  
<script setup lang="ts">
  import { ref } from 'vue'
  //import LoginForm from '@/components/auth/LoginForm.vue'
  
  definePageMeta({
    layout: 'default'
  })


</script>
  
<style>
/* Add your styles here */
  #app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>
 