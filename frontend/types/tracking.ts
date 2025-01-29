export interface TrackingEvent {
  eventName: string
  category?: string
  label?: string
  value?: number
  properties?: Record<string, any>
}
