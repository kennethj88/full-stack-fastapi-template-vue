export default defineNuxtPlugin(() => {
  const { trackEvent, trackPageView } = useEventTracking()

  // Track page views automatically
  const router = useRouter()
  router.afterEach((to) => {
    trackPageView(to.name as string, {
      path: to.path,
      query: to.query
    })
  })

  return {
    provide: {
      track: trackEvent,
      trackPage: trackPageView
    }
  }
}) 