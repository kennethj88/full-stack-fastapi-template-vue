export const useTheme = () => {
  // Use useState to persist theme across page refreshes
  const isDarkMode = useState('isDarkMode', () => true)

  // Toggle theme function
  const toggleTheme = () => {
    isDarkMode.value = !isDarkMode.value
    
    // Update document class for Tailwind/DaisyUI
    if (process.client) {
      if (isDarkMode.value) {
        document.documentElement.classList.add('dark')
        document.documentElement.setAttribute('data-theme', 'dark')
      } else {
        document.documentElement.classList.remove('dark')
        document.documentElement.setAttribute('data-theme', 'light')
      }
    }
  }

  // Initialize theme on client side
  onMounted(() => {
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark')
      document.documentElement.setAttribute('data-theme', 'dark')
    }
  })

  return {
    isDarkMode,
    toggleTheme
  }
} 