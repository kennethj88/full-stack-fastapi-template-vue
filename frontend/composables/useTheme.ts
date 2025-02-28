/*
import { ref } from 'vue'

export function useTheme() {
  const isDarkMode = true //ref(false)

  const initTheme = () => {
    if (import.meta.client) {
       // isDarkMode.value = document.documentElement.classList.contains('dark')
        
    }
  }

 

  const toggleTheme = () => {
    isDarkMode.value = !isDarkMode.value
    if (import.meta.client) {
        
        if (isDarkMode.value) {
            document.documentElement.classList.add('dark')
            document.documentElement.setAttribute('data-theme', 'dark')
        } else {
            document.documentElement.classList.remove('dark')
            document.documentElement.setAttribute('data-theme', 'light')
        }
    }
  }

  return {
    isDarkMode,
    toggleTheme,
    initTheme
  }
} 

*/