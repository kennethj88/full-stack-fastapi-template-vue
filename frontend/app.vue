<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()

useHead({
  script: [
    {
      src: 'https://cloud.umami.is/script.js',
      'data-website-id': useRuntimeConfig().public.umamiWebsiteId,
      async: true,
      defer: true,
    }
  ]
})

// Initialize auth store
onMounted(async () => {
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
  <div>
    <NuxtLayout>
      <!-- start nuext page slot-->
      <NuxtPage />
        <!-- end nuext page slot-->
    </NuxtLayout>
  </div>
</template>
