<script setup lang="ts">
import { ref, reactive, onMounted} from 'vue'
import { useAuthStore } from '~/stores/auth'
import GoogleButton from './GoogleButton.vue'
import BaseInput from '~/components/ui/BaseInput.vue'



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
  <div class="login-container flex flex-col items-stretch p-6 md:p-8">
    <h3 class="mt-8 text-center text-xl font-semibold md:mt-12">Login</h3>
    <h3 class="mt-2 text-center text-sm text-base-content/70">
      Seamless Access, Secure Connection: Your Gateway to a Personalized Experience.
    </h3>

    <form @submit.prevent="handleSubmit" class="mt-6 md:mt-10">
      <div class="form-control">
        <BaseInput
          labelTxt="Email Address"
          iconifyIcon="lucide:mail"
          v-model="form.email"
          type="email"
          id="username"
          required
          placeholder="Email Address"
          autocomplete="email"
          :error="errors.email"
        />
      </div>

      <div class="form-control mt-3">
        <BaseInput
          labelTxt="Password"
          iconifyIcon="lucide:key-round"
          v-model="form.password"
          :type="showPassword ? 'text' : 'password'"
          id="password"
          required
          placeholder="Password"
          autocomplete="current-password"
          :error="errors.password"
        >
          <button 
            type="button" 
            class="btn btn-circle btn-ghost btn-xs hover:bg-base-content/10" 
            @click.stop="toggleShowPassword"
          >
            <Icon
              :name="showPassword ? 'lucide:eye-off' : 'lucide:eye'"
              height="16"
              class="text-base-content/80"
            />
          </button>
        </BaseInput>

        <div class="flex justify-end mt-1">
          <nuxt-link to="/forgot-password" class="text-xs text-base-content/80">
            Forgot Password?
          </nuxt-link>
        </div>
      </div>

      <div class="mt-4 md:mt-6">
        <span v-if="authStore.error" class="error text-error text-sm block mb-2">
          {{ authStore.error }}
        </span>
        <button 
          class="btn btn-primary btn-block gap-2 text-base" 
          type="submit" 
          :disabled="authStore.loading"
        >
          <Icon name="lucide:log-in" height="16" />
          {{ authStore.loading ? 'Logging in...' : 'Log In' }}
        </button>
      </div>

      <!-- Social Login Divider -->
      <div class="relative mt-6">
        <div class="absolute inset-0 flex items-center">
          <div class="w-full border-t border-base-content/10" />
        </div>
        <div class="relative flex justify-center text-sm">
          <span class="px-2 bg-base-100 text-base-content/70">Or </span>
        </div>
      </div>

      <div class="mt-6 text-center">
        <GoogleButton @login-success="emit('login-success')" @requires-password="handlePasswordRequired" />
      </div>
    </form>

    <p class="mt-6 text-center text-sm text-base-content/70">
      Don't have an account? <nuxt-link to="/sign-up" class="text-base-content/80">Sign up</nuxt-link>
    </p>
  </div>
</template>
  
  
  <style scoped>
  </style>