// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  /*devtools: {
    enabled: false,

    timeline: {
      enabled: false
    }
  },*/
  modules: [
    '@pinia/nuxt',
    '@vueuse/nuxt',
   // '@nuxtjs/tailwindcss',
    '@nuxt/icon',
    '@nuxtjs/color-mode',
   //  '@nuxtjs/google-fonts',
   /*["@sentry/nuxt/module", {
      sourceMapsUploadOptions: {
        org: "bongodaa",
        project: "bongolocal",
        authToken: process.env.SENTRY_AUTH_TOKEN,
      },
      sourcemap: {
        hidden: true,
      },
      client: {
        tracesSampleRate: 1.0,
        replaysSessionSampleRate: 0.1,
        replaysOnErrorSampleRate: 1.0,
      },
      server: {
        disabled: true
      }
    }] */
  ],
  //@ts-ignore
  googleFonts: {
    families: {
      'DM+Sans': {
        wght: ['400', '500', '600', '700', '800', '1000'],
      }
    },
    display: 'swap',
    preload: true,
    download: true, // Add this to download fonts instead of using CDN
    base64: false, // Keep this false for better caching
  },
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
      umamiWebsiteId: process.env.UMAMI_WEBSITE_ID,
      enableDevTracking: true,
      sentryDsn: process.env.SENTRY_DSN || '',
      // Add other tracking-related config here
    }
  },
  colorMode: {
    classSuffix: ''
  },
  css: [
 //   '@/assets/css/tailwind.css'
  ],
 /* tailwindcss: {
    cssPath: '@/assets/css/tailwind.css',
    configPath: './tailwind.config.ts',
    exposeConfig: false,
    viewer: true,
  },*/
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
   // '/dashboard/**': { ssr: false },
   // '/zero/': { ssr: false },
  },
  nitro: {
    prerender: {
      routes: ['/'],
      crawlLinks: true,
      failOnError: false,
    },
    routeRules: {
      '/_nuxt/**': {
        headers: {
          'Cache-Control': process.env.NODE_ENV === 'development' 
            ? 'no-store, no-cache, must-revalidate, proxy-revalidate'
            : 'public, max-age=31536000, immutable'
        }
      }
    }
  },
  
})