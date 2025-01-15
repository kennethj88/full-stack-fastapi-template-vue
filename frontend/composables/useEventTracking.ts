import { useRuntimeConfig } from '#app'

export interface TrackingEvent {
  eventName: string
  category?: string
  label?: string
  value?: number
  properties?: Record<string, any>
}

export const useEventTracking = () => {
  const trackIdentify = async (userToken: string, properties = {}) => {
    const config = useRuntimeConfig()
    console.log('identify',userToken,properties)
    window?.umami?.identify({ email: userToken  });
  }

  const trackEvent = async ({
    eventName,
    category = 'general',
    label,
    value,
    properties = {}
  }: TrackingEvent) => {
    const config = useRuntimeConfig()
    try {
      // You can add conditions here to disable tracking in dev mode
      if (import.meta.dev && !config.public.enableDevTracking) return

      // Construct the event payload
      const eventPayload = {
        event: eventName,
        category,
        label,
        value,
        timestamp: new Date().toISOString(),
        ...properties
      }

      // Here you can implement different tracking services
      // Example: Google Analytics, Mixpanel, or custom backend
      console.log('Event tracked:', eventPayload)
      
      // Example of sending to your backend
      //track umami
      window.umami?.track(eventName,eventPayload); 

    } catch (error) {
      console.error('Failed to track event:', error)
    }
  }

  // Predefined tracking methods for common events
  const trackPageView = (pageName: string, properties = {}) => {
    return trackEvent({
      eventName: 'page_view',
      category: 'navigation',
      label: pageName,
      properties
    })
  }

  return {
    trackEvent,
    trackIdentify,
    trackPageView
  }
} 