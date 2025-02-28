import { defineNuxtPlugin } from '#app'
import * as Sentry from '@sentry/nuxt'

export default defineNuxtPlugin((nuxtApp) => {
  Sentry.init({
    dsn: process.env.SENTRY_DSN,
    
    // Performance monitoring settings
    tracesSampleRate: process.env.NODE_ENV === 'production' ? 0.1 : 1.0,
    
    // Session replay settings
    replaysSessionSampleRate: process.env.NODE_ENV === 'production' ? 0.1 : 1.0,
    replaysOnErrorSampleRate: 1.0,

    // Environment
    environment: process.env.NODE_ENV,

    // Required for Nuxt integration
    
  })
}) 
  