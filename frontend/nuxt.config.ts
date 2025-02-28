// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@pinia/nuxt',
    '@vueuse/nuxt',
    '@nuxt/icon',
    '@nuxtjs/color-mode',
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@sentry/nuxt/module'
  ],
  imports: {
    dirs: ['stores']
  },
  pinia: {
    storesDirs: ['./stores/**'],
  },
  //css: ['~/assets/css/main.css'],
  css: ['~/assets/css/tailwind.css'],
  tailwindcss: {
    viewer: { endpoint: '/_tailwind', exportViewer: true },
    cssPath: ['~/assets/css/tailwind.css', { injectPosition: "first" }],
    exposeConfig: true,
    editorSupport: true
    // and more...
  },
  
  postcss: {
    plugins: {
      'postcss-import': {
        // This disables the rule for @import statements position
        skipDuplicates: false,
        path: ['~/assets/css/'],
        order: false
      },
      // Other plugins like tailwindcss, autoprefixer, etc.
    }
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
      umamiWebsiteId: process.env.UMAMI_WEBSITE_ID,
      enableDevTracking: true,
      sentryDsn: process.env.SENTRY_DSN || '',
      // Add other tracking-related config here
    }
  },
  app: {
    head: {
      title: 'FastAPI + Nuxt3 Starter',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' }
      ],
      script: [
        {
          src: 'https://cloud.umami.is/script.js',
          'data-website-id': process.env.UMAMI_WEBSITE_ID,
          async: true,
          defer: true
        }
      ]
    }
  },
  colorMode: {
    classSuffix: ''
  },
  routeRules: {
    '/**': { ssr: false },
    // '/zero/': { ssr: false },
   },
  nitro: {
    routeRules: {
      '/_nuxt/**': {
        headers: {
          'Cache-Control': process.env.NODE_ENV === 'development'
            ? 'no-store, no-cache, must-revalidate, proxy-revalidate'
            : 'public, max-age=31536000, immutable'
        }
      },
      //'/_nuxt/assets/**/*.css': { // Use a wildcard to match any CSS file under /_nuxt/assets/
      //  headers: {
      //    'Content-Type': process.env.NODE_ENV === 'development' ? 'text/javascript; charset=utf-8' : 'text/css; charset=utf-8', // Corrected MIME type for CSS
       //   'X-Content-Type-Options': 'nosniff'
      //  }
     // },
  },
},
experimental: {
    //inlineSSRStyles: false,
    viewTransition: true,
    renderJsonPayloads: true
  }
})


/*
     */
    //rm -f /tmp/nitro/worker-40-2.sock
