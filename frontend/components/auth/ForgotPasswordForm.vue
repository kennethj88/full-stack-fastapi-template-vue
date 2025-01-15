<template>
  <div class="grid min-h-screen grid-cols-12 overflow-auto">
   
  <!-- Form Panel -->
  <div class="col-span-12 lg:col-span-5 xl:col-span-4 2xl:col-span-3">
    <div class="flex flex-col items-stretch p-6 md:p-8">
      

      <!-- Form Content -->
      <h3 class="mt-8 text-center text-xl font-semibold md:mt-12">Forgot Password</h3>
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
            id="email"
            required
            placeholder="Email Address"
            autocomplete="email"
            :error="errors.email"
          />
        </div>

        

        <button
          type="submit"
          :disabled="authStore.loading"
          class="btn btn-primary btn-block gap-2 text-base mt-4 md:mt-6"
        >
          <Icon name="lucide:mail-plus" height="16" />
          {{ authStore.loading ? 'Sending...' : 'Send a reset link' }}
        </button>

        <div v-if="authStore.error" class="mt-4 text-error text-sm text-center">
          {{ authStore.error }}
        </div>

        <div v-if="success" class="mt-4 text-success text-sm text-center">
          Recovery email sent! Please check your inbox.
        </div>

        <p class="mt-4 text-center text-sm text-base-content/80 md:mt-6">
          I have already to
          <nuxt-link to="/login" class="text-primary hover:underline">Login</nuxt-link>
        </p>
      </form>
    </div>
  </div>
</div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useAuthStore } from '~/stores/auth'
import BaseInput from '~/components/ui/BaseInput.vue'

const authStore = useAuthStore()
const success = ref(false)

const form = reactive({
  email: '',
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