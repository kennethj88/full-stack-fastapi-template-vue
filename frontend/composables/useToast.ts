import { ref } from 'vue'

interface ToastOptions {
  message: string
  type?: 'success' | 'error' | 'info'
  duration?: number
}

export const useToast = () => {
  const isVisible = ref(false)
  const message = ref('')
  const type = ref<'success' | 'error' | 'info'>('info')

  const showToast = (options: ToastOptions) => {
    message.value = options.message
    type.value = options.type || 'info'
    isVisible.value = true

    setTimeout(() => {
      isVisible.value = false
    }, options.duration || 3000)
  }

  return {
    isVisible,
    message,
    type,
    showToast
  }
} 