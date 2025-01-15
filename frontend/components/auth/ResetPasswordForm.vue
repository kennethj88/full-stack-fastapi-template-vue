<template>
  <div class="grid min-h-screen grid-cols-12 overflow-auto">
    <!-- Form Panel -->
    <div class="col-span-12 lg:col-span-5 xl:col-span-4 2xl:col-span-3">
      <div class="flex flex-col items-stretch p-6 md:p-8">
        <!-- Form Content -->
        <h3 class="mt-8 text-center text-xl font-semibold md:mt-12">Reset Password</h3>
        <h3 class="mt-2 text-center text-sm text-base-content/70">
          Create a new secure password for your account
        </h3>

        <form @submit.prevent="handleSubmit" class="mt-6 md:mt-10">
          <div class="form-control">
            <BaseInput
              labelTxt="New Password"
              iconifyIcon="lucide:key-round"
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              id="password"
              required
              placeholder="Enter new password"
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
          </div>

          <div class="form-control mt-4">
            <BaseInput
              labelTxt="Confirm Password"
              iconifyIcon="lucide:key-round"
              v-model="form.confirmPassword"
              :type="showPassword ? 'text' : 'password'"
              id="confirmPassword"
              required
              placeholder="Confirm new password"
              :error="errors.confirmPassword"
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
          </div>

          <button
            type="submit"
            :disabled="authStore.loading"
            class="btn btn-primary btn-block gap-2 text-base mt-6"
          >
            <Icon name="lucide:check" height="16" />
            {{ authStore.loading ? 'Resetting...' : 'Reset Password' }}
          </button>

          <div v-if="authStore.error" class="mt-4 text-error text-sm text-center">
            {{ authStore.error }}
          </div>

          <div v-if="success" class="mt-4 text-success text-sm text-center">
            Password reset successful! You can now login with your new password.
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useAuthStore } from '~/stores/auth'
import { useRoute, useRouter } from 'vue-router'
import BaseInput from '~/components/ui/BaseInput.vue'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const success = ref(false)
const showPassword = ref(false)

const form = reactive({
  password: '',
  confirmPassword: ''
})

const errors = reactive({
  password: '',
  confirmPassword: ''
})

const toggleShowPassword = () => {
  showPassword.value = !showPassword.value
}

const validateForm = () => {
  let isValid = true
  errors.password = ''
  errors.confirmPassword = ''

  if (!form.password) {
    errors.password = 'Password is required'
    isValid = false
  } else if (form.password.length < 8) {
    errors.password = 'Password must be at least 8 characters'
    isValid = false
  }

  if (!form.confirmPassword) {
    errors.confirmPassword = 'Please confirm your password'
    isValid = false
  } else if (form.password !== form.confirmPassword) {
    errors.confirmPassword = 'Passwords do not match'
    isValid = false
  }

  return isValid
}

const handleSubmit = async () => {
  if (validateForm()) {
    const token = route.query.token as string
    if (!token) {
      authStore.error = 'Invalid reset token'
      return
    }

    const result = await authStore.resetPassword(token, form.password)
    if (result) {
      success.value = true
      form.password = ''
      form.confirmPassword = ''
      setTimeout(() => {
        router.push('/login')
      }, 2000)
    }
  }
}
</script> 