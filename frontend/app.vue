<script setup>
import { useAuthStore } from '@/stores/auth'
const auth   = useAuthStore()

// Initialize auth store
onBeforeMount(async () => {
  if (import.meta.client && !auth.initialized) {
    await auth.init()
  }
})

</script>



<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
