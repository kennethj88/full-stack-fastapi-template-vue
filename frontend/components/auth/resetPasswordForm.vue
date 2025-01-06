<template>
  <div class="flex flex-col justify-center items-center min-h-screen">
    <form @submit.prevent="handleSubmit" class="max-w-sm w-full p-6 space-y-4">
      <img
        :src="logo"
        alt="FastAPI logo"
        class="h-auto max-w-[16rem] mx-auto mb-4"
      />
   
      <div class="form-group">
        <label for="password" class="sr-only">Password</label>
        <input
          id="password"
          v-model="form.values.password"
          placeholder="Password"
          type="password"
          class="w-full rounded-md border p-2"
        />
        <span v-if="form.errors.password" class="text-red-500 text-sm">
          {{ form.errors.password }}
        </span>
      </div>

      <div class="form-group">
        <label for="confirmPassword" class="sr-only">Confirm Password</label>
        <input
          id="confirmPassword"
          v-model="form.values.confirmPassword"
          placeholder="Repeat Password"
          type="password"
          class="w-full rounded-md border p-2"
        />
        <span v-if="form.errors.confirmPassword" class="text-red-500 text-sm">
          {{ form.errors.confirmPassword }}
        </span>
      </div>

      <button 
        type="submit" 
        class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 disabled:opacity-50"
        :disabled="isSubmitting"
      >
        {{ isSubmitting ? 'Resetting...' : 'Reset Password' }}
      </button>
    </form>
  </div>
</template>


<script setup>
import { ref, reactive } from 'vue';
import useAuth from '@/composables/useAuth' // Custom composable for authentication
import logo from '@/public/assets/images/fastapi-logo.svg'

const { login, error, resetError } = useAuth()
const isSubmitting = ref(false)

const form = reactive( 
      {   errors:{
          },
          values:{
              fullName: '',
              email: '',
              password: '',
              confirmPassword: ''
          }
  });

const validateForm = () => {
    form.errors =  {};
    if (form.values.password.length < 6) {
      form.errors.password = 'Password must be at least 6 characters long.';
    }
    if (form.values.password !== form.values.confirmPassword) {
      form.errors.confirmPassword = 'Passwords do not match.';
    }
    return Object.keys(form.errors).length === 0
  }
  
  
  const handleSubmit = async () => {
    console.log('submit')
    if (validateForm()) {
      try {
        isSubmitting.value = true
        await resetPassword(form.values.password)
        router.push('/') // Redirect to home on successful login
      } catch (err) {
        //special error handling
      } finally {
        isSubmitting.value = false
      }
    }
  }

   

</script>

  <style scoped>
  /* Add your styles here */
  </style>
    
  