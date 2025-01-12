// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: {
    enabled: true,

    timeline: {
      enabled: true
    }
  },
  modules: [
    '@pinia/nuxt',
    '@nuxtjs/tailwindcss',
    '@vueuse/nuxt',
    '@nuxtjs/color-mode',
    '@nuxt/icon'
  ],
  imports: {
    dirs: ['stores']
  },
  pinia: {
    storesDirs: ['./stores/**'],
  },
  typescript: {
    strict: true,
    typeCheck: true,
    shim: false
  },
  runtimeConfig: {
    public: {
      apiUrl: process.env.VITE_API_URL || 'http://localhost:8000',
      googleClientId: process.env.GOOGLE_CLIENT_ID,
      umamiWebsiteId: process.env.UMAMI_WEBSITE_ID
    }
  },
  colorMode: {
    classSuffix: ''
  },
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.css',
    exposeConfig: true,
    viewer: true,
    // and more...
  },
  app: {
    head: {
      title: 'FastAPI + Nuxt3 Starter',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' }
      ]
    }
  },
  routeRules: {
    '/dashboard/**': { ssr: false },
  },
  nitro: {
    prerender: {
      // Customize which routes get preloaded
      routes: ['/']
    }
  }
})