/*
import type { TrackingEvent } from '~/types/tracking'

export default defineNuxtPlugin((nuxtApp) => {
    // Define the tracking functions first so they can be referenced
    const trackEvent = ({
        eventName,
        category = 'general',
        label,
        value,
        properties = {}
    }: TrackingEvent) => {
        if (import.meta.client) {
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
                window?.umami?.track(eventName, eventPayload)

            } catch (error) {
                console.error('Failed to track event:', error)
            }
            return true;
        }
    }

    const trackIdentify = (userToken: string, properties?: Record<string, any>) => {
        if (import.meta.client) {
            console.log('identify', userToken, properties)
            window?.umami?.identify({ email: userToken })
        }
        return true;
    }

    const trackPageView = (pageName: string, properties = {}) => {
        return trackEvent({
            eventName: 'page_view',
            category: 'navigation',
            label: pageName,
            ...properties
        })
    }

    // Wait for app to be mounted before setting up router hooks
    nuxtApp.vueApp.use(() => {
        const router = useRouter()
        router.afterEach((to) => {
            // Only track page views on client-side
            if (import.meta.client) {
                trackPageView(to.name as string, {
                    path: to.path,
                    query: to.query
                })
            }
        })
    })

    return {
        provide: {
            trackEvent,
            trackIdentify,
            trackPageView
        }
    }
}) 

*/