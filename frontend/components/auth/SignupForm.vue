<template>
  <div class="form-container">
    <img :src="logo" alt="Logo" class="logo" />
    <h2>Sign Up</h2>
    
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="fullName">Full Name</label>
        <BaseInput
          v-model="form.fullName"
          type="text"
          id="fullName"
          placeholder="Enter your full name"
        />
        <span v-if="errors.fullName" class="error">{{ errors.fullName }}</span>
      </div>

      <div class="form-group">
        <label for="email">Email</label>
        <BaseInput
          v-model="form.email"
          type="email"
          id="email"
          required
          placeholder="Enter your email"
        />
        <span v-if="errors.email" class="error">{{ errors.email }}</span>
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <BaseInput
          v-model="form.password"
          :type="showPassword ? 'text' : 'password'"
          id="password"
          required
          placeholder="Create a password"
        />
        <button 
          type="button" 
          class="show-password-btn"
          @click="toggleShowPassword"
        >
          {{ showPassword ? 'Hide' : 'Show' }} password
        </button>
        <span v-if="errors.password" class="error">{{ errors.password }}</span>
      </div>

      <button 
        type="submit" 
        class="btn btn-primary submit-btn"
        :disabled="authStore.loading"
      >
        {{ authStore.loading ? 'Creating Account...' : 'Create Account' }}
      </button>

      <div v-if="authStore.error" class="error">
        {{ authStore.error }}
      </div>

      <p class="login-link">
        Already have an account? <nuxt-link to="/login">Log in</nuxt-link>
      </p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import BaseInput from '~/components/ui/BaseInput.vue'
import { useAuthStore } from '~/stores/auth'

const logo = '/images/fastapi-logo.svg'

const router = useRouter()
const authStore = useAuthStore()

const showPassword = ref(false)
const form = reactive({
  fullName: '',
  email: '',
  password: ''
})

const errors = reactive({
  fullName: '',
  email: '',
  password: ''
})

const emit = defineEmits<{
  'signup-success': []
}>()

const toggleShowPassword = () => {
  showPassword.value = !showPassword.value
}

const validateForm = () => {
  let isValid = true
  errors.fullName = ''
  errors.email = ''
  errors.password = ''

  if (!form.email) {
    errors.email = 'Email is required'
    isValid = false
  }

  if (!form.password) {
    errors.password = 'Password is required'
    isValid = false
  } else if (form.password.length < 8) {
    errors.password = 'Password must be at least 8 characters'
    isValid = false
  }

  return isValid
}

const handleSubmit = async () => {
  if (validateForm()) {
    try {
      const success = await authStore.signup({
        email: form.email,
        password: form.password,
        full_name: form.fullName
      })


      if (success) {
        console.log('signup form:success--do login')
        await authStore.login({email: form.email,
                               password: form.password})
        
        emit('signup-success')
      }
    } catch (error) {
      console.error('Signup error:', error)
    }
  }
}
</script>

<style scoped>

</style> 