interface UmamiTracker {
  track: (eventName: string, eventData?: Record<string, any>) => void;
  identify: (data: { email: string }) => void;
}

declare global {
  interface Window {
    umami?: UmamiTracker;
  }
}

export {}; 