<script setup lang="ts">
import { ref, reactive, onMounted} from 'vue'
import { useAuthStore } from '~/stores/auth'
import logo from '@/public/assets/images/fastapi-logo.svg'
import GoogleButton from './GoogleButton.vue'



console.log('LoginForm script executing')


const emit = defineEmits<{
  'login-success': []
}>()

const router = useRouter()
const authStore = useAuthStore()


const showPassword = ref(false)
const errors = reactive({
  email: '',
  password: ''
})

const form = reactive({
  email: '',
  password: ''
})

const toggleShowPassword = () => {
  console.log('toggle show password')
  showPassword.value = !showPassword.value
}

const validateForm = () => {
  let isValid = true
  errors.email = ''
  errors.password = ''

  if (!form.email) {
    errors.email = 'Email is required'
    isValid = false
  }

  if (!form.password) {
    errors.password = 'Password is required'
    isValid = false
  }

  return isValid
}

 
const handleSubmit = async (event: Event) => {
  console.log('form submitted')
  event.preventDefault()
  
  if (validateForm()) {
    try {
      console.log('Attempting login with:', { email: form.email })
      const success = await authStore.login({
        email: form.email,
        password: form.password
      })
      
      if (success) {
        console.log('Login successful')
        emit('login-success')
      } else {
        console.log('Login failed:', authStore.error)
      }
    } catch (error) {
      console.error('Login error:', error)
    }
  } else {
    console.log('Form validation failed:', errors)
  }

  
}

const showPasswordModal = ref(false)
const pendingGoogleData = ref(null)

interface GooglePasswordData {
  email: string
  googleToken: string
}
const handlePasswordRequired = (data: GooglePasswordData) => {
  pendingGoogleData.value = data as unknown as null
  showPasswordModal.value = true
}
</script>

<template>
    <div class="login-container">
    <div class="text-green-500">Component Mounted!</div>
    
      <img :src="logo" alt="Logo" class="logo" />
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Email</label>
          <input
            v-model="form.email"
            type="email"
            id="username"
            required
            placeholder="Email"
            autocomplete="email"
          />
          <span v-if="errors.email">{{ errors.email }}</span>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            v-model="form.password"
            :type="showPassword ? 'text' : 'password'"
            id="password"
            required
            placeholder="Password"
             autocomplete="current-password"
          />
          <button type="button" 
                   class="show-password-btn"
                  @click.stop="toggleShowPassword">
            {{ showPassword ? 'Hide' : 'Show' }} password
          </button>
        </div>
        <nuxt-link to="/recover-password">Forgot password?</nuxt-link>
        
        <div>
        <span v-if="authStore.error" class="error">{{ authStore.error }}</span>
        <button type="submit" :disabled="authStore.loading">
          {{ authStore.loading ? 'Logging in...' : 'Log In' }}
        </button>
      </div>
      
        <p>
          Don't have an account? <nuxt-link to="/sign-up">Sign up</nuxt-link>
        </p>
      </form>

      <div class="mt-6">
        <div class="relative">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-300" />
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-2 bg-white text-gray-500">Or continue with</span>
          </div>
        </div>

        <div class="mt-6">
          <GoogleButton @login-success="emit('login-success')" @requires-password="handlePasswordRequired" />
        </div>
      </div>
    </div>
  </template>
  
  
  <style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 2rem;
  }
  
  .logo {
    max-width: 200px;
    margin-bottom: 2rem;
  }
  
  .form-group {
    margin-bottom: 1rem;
    width: 100%;
    max-width: 320px;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
  }
  
  input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 0.75rem;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 1rem;
  }
  
  button:disabled {
    background-color: #9ca3af;
    cursor: not-allowed;
  }
  
  .error {
    color: #ef4444;
    font-size: 0.875rem;
    margin-top: 0.5rem;
  }
  
  a {
    color: #4f46e5;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>