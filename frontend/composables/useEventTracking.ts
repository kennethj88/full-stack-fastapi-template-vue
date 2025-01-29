/*
import type { TrackingEvent } from '~/types/tracking'

export const useEventTracking = () => {
  const trackIdentify = async (userToken: string, properties = {}) => {
    const { $trackIdentify } = useNuxtApp()
    return $trackIdentify(userToken, properties)
  }

  const trackEvent = async ({
    eventName,
    category = 'general',
    label,
    value,
    properties = {}
  }: TrackingEvent) => {
    const { $trackEvent } = useNuxtApp()
    return $trackEvent({eventName, category, label, value, ...properties})
  }
 
  // Predefined tracking methods for common events
  const trackPageView = (pageName: string, properties = {}) => {
    const { $trackPageView } = useNuxtApp()
    return $trackPageView(pageName, properties)
  }

  return {
    trackEvent,
    trackIdentify,
    trackPageView
  }
} 

*/