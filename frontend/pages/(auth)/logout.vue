<template>
    <div id="app">
        Logging out ...
  </div>
</template>
  
<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useAuthStore } from '@/stores/auth'
  const router = useRouter()
  const auth = useAuthStore()
  
  onMounted(async () => {
    auth.logout()
    router.push('/login')
  })
  
  
</script>
  
<style>

</style>