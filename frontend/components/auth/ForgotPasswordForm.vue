<template>
  <div class="form-container">
    <img :src="logo" alt="Logo" class="logo" />
    <h2>Recover Password</h2>
    
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="email">Email</label>
        <input
          v-model="form.email"
          type="email"
          id="email"
          required
          placeholder="Enter your email"
        />
        <span v-if="errors.email" class="error">{{ errors.email }}</span>
      </div>

      <button type="submit" :disabled="authStore.loading">
        {{ authStore.loading ? 'Sending...' : 'Send Recovery Email' }}
      </button>

      <div v-if="authStore.error" class="error">
        {{ authStore.error }}
      </div>

      <div v-if="success" class="success">
        Recovery email sent! Please check your inbox.
      </div>

      <p class="mt-4">
        Remember your password? <nuxt-link to="/login">Log in</nuxt-link>
      </p>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useAuthStore } from '~/stores/auth'

// Update the logo import to use the public path
const logo = '/images/fastapi-logo.svg'

const authStore = useAuthStore()
const success = ref(false)

const form = reactive({
  email: ''
})

const errors = reactive({
  email: ''
})

const validateForm = () => {
  let isValid = true
  errors.email = ''

  if (!form.email) {
    errors.email = 'Email is required'
    isValid = false
  }

  return isValid
}

const handleSubmit = async () => {
  if (validateForm()) {
    const result = await authStore.forgotPassword(form.email)
    if (result) {
      success.value = true
      form.email = ''
    }
  }
}
</script>

<style scoped>
.form-container {
  width: 100%;
  max-width: 400px;
  padding: 2rem;
}

.logo {
  max-width: 200px;
  margin: 0 auto 2rem;
  display: block;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1rem;
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

.success {
  color: #10b981;
  font-size: 0.875rem;
  margin-top: 0.5rem;
  text-align: center;
}

a {
  color: #4f46e5;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style> 