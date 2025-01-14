<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()

useHead({
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/images/favicons/favicon.ico' },
    { rel: 'apple-touch-icon', sizes: '180x180', href: '/images/favicons/apple-touch-icon.png' },
    { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/images/favicons/favicon-32x32.png' },
    { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/images/favicons/favicon-16x16.png' },
    { rel: 'manifest', href: '/images/favicons/site.webmanifest' }
  ],
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
