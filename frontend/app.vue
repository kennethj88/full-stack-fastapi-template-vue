<script setup lang="ts">
import { useAuthStore } from '@/stores/auth'
import { useTheme } from '@/composables/useTheme'
const auth = useAuthStore()
const { isDarkMode } = useTheme()

useHead({
  link: [
    { rel: 'icon', type: 'image/x-icon', href: '/_nuxt/assets/images/favicons/favicon.ico' },
    { rel: 'apple-touch-icon', sizes: '180x180', href: '/_nuxt/assets/images/favicons/apple-touch-icon.png' },
    { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/_nuxt/assets/images/favicons/favicon-32x32.png' },
    { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/_nuxt/assets/images/favicons/favicon-16x16.png' },
    { rel: 'manifest', href: '/_nuxt/assets/images/favicons/site.webmanifest' }
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

// Initialize theme on app load
onMounted(() => {
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark')
    document.documentElement.setAttribute('data-theme', 'dark')
  } else {
    document.documentElement.classList.remove('dark')
    document.documentElement.setAttribute('data-theme', 'light')
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
