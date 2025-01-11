<script setup>
import { useAuthStore } from '@/stores/auth'
const auth   = useAuthStore()

// Initialize auth store
onBeforeMount(async () => {
  if (import.meta.client && !auth.initialized) {
    try {
      await auth.init()
    } catch (error) {
      console.error('Auth initialization error:', error)
    }
  }
})

</script>



<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
