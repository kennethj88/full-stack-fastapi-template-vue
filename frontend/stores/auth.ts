import { defineStore, skipHydrate } from 'pinia'
import { useAxiosInstance } from '@/composables/api/axiosInstance'
import { authApi } from '@/composables/api/auth'
import type { LoginCredentials, SignupCredentials, User } from '@/types'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  
  // Properly declare refs
  const user = ref<User | null>(null)
  const error = ref<string | null>(null)
  const loading = ref(false)
  const initialized = ref(false)

  //const hydrated = ref(false)

  // Computed property for authentication status
  const isAuthenticated = computed((): boolean => {
    const accessToken = useCookie('access_token')
    return initialized.value && !!accessToken.value && !!user.value
  })

  const setUser = (userData: User) => {
    console.log('auth store:set user',userData)
    user.value = userData
    return true
  }

  const updateUser = (userData: Partial<User>) => {
    if (user.value) {
      user.value = { ...user.value, ...userData }
    }
  }

  //const getRole = computed(() => user?.value?.role || '')

  const setToken = (accessToken: string) => {
    const access = useCookie('access_token')
    access.value = accessToken
  }

  const cleanUser = () => {
    const access = useCookie('access_token')
    const refresh = useCookie('refresh_token')
    error.value = ''
    access.value = null
    refresh.value = null
    user.value = null
  }

  const getToken = computed(() => {
    const access = useCookie('access_token')
    return access.value
  })

  async function init() {
    console.log('auth store: init, initilized:',initialized.value)
    if (initialized.value) return
    console.log('auth store: init, getToken', getToken.value)
    if (import.meta.client && getToken.value) {
      console.log('auth store: init, await refreshUser')
      await refreshUser()
        //hydrated.value = true
    }
    initialized.value = true
  }


  async function forgotPassword(email: string) {
    try {
      loading.value = true
      error.value = null
      await authApi.forgotPassword(email)
      return true
    } catch (error: any) {
      error.value = error.response?.data?.detail || 'An error occurred'
      return false
    } finally {
      loading.value = false
    }
  }

  async function login(payload: LoginCredentials) {
    loading.value = true
    error.value = null
    
    try {
        const response = await authApi.login(payload)
        if (response?.access_token) {
            setToken(response.access_token)
            const userData = await authApi.getCurrentUser()
            if (userData) {
              setUser(userData)
              return true
            }
          }
          return false
    } catch (error: any) {
        error.value = error.response?.data?.detail || 'An error occurred during login'
        console.log('login error', error)
        return false
    } finally {
        loading.value = false
    }
  }

  async function signup(payload: SignupCredentials) {
    loading.value = true
    error.value = null
    try {
      console.log('sign up: try')
      const response = await authApi.signup(payload)
        if (response?.id) {
            console.log('sign up: success', response.user)
            //setToken(response.access_token) //handled seperately
            setUser(response)
            loading.value = false
            return true
        }
        loading.value = false
        return false
    } catch (err: any) {
        error.value = err.response?.data?.detail || 'An error occurred during signup'
        loading.value = false
      return false
    } 
  }

  async function refreshUser() {
    console.log('auth store:refresh user start')
    try {
      const updatedUser = await authApi.getCurrentUser()
      setUser(updatedUser)
    } catch (err: any) {
      console.log(err.response?.data?.detail || 'Failed to refresh user data')
      return false
    }
  }

  function logout() {
    console.log('logout called')
    cleanUser()
    navigateTo('/login')
    return 
  }

  async function googleLogin(token: string) {
    loading.value = true
    error.value = null
    
    try {
      const response = await authApi.googleLogin(token)
      
      if (response.requires_password) {
        return response
      }
      
      if (response.access_token) {
        setToken(response.access_token)
        const userData = await authApi.getCurrentUser()
        if (userData) {
          setUser(userData)
          return true
        }
      }
      return false
    } catch (error: any) {
      error.value = error.response?.data?.detail || 'An error occurred during Google login'
      return false
    } finally {
      loading.value = false
    }
  }

  async function linkGoogleAccount(token: string, password: string) {
    loading.value = true
    error.value = null
    
    try {
      const response = await authApi.linkGoogleAccount(token, password)
      
      if (response.access_token) {
        setToken(response.access_token)
        const userData = await authApi.getCurrentUser()
        if (userData) {
          setUser(userData)
          return true
        }
      }
      return false
    } catch (error: any) {
      error.value = error.response?.data?.detail || 'An error occurred while linking account'
      return false
    } finally {
      loading.value = false
    }
  }

  // ... existing signup, login, refreshUser, and logout functions ...
  
  return {
    // State
    user: skipHydrate(user),
    error: skipHydrate(error),
    loading: skipHydrate(loading),
    initialized: skipHydrate(initialized),

    // Computed
    isAuthenticated,

    // Actions
    init,
    signup,
    login,
    logout,
    refreshUser,
    forgotPassword,
    setUser,
    updateUser,
    setToken,
    cleanUser,
    googleLogin,
    linkGoogleAccount
  }
},
{
    //persist: true,
},
)