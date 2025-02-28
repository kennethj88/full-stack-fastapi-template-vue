<template>
  <div class="min-h-screen">
      <LoginForm
      @login-success="loginSuccess"
    />
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import LoginForm from '~/components/auth/LoginForm.vue'
  import { useAuthStore } from '@/stores/auth'
  
  const router = useRouter()
  const auth = useAuthStore()

  const loginSuccess = async () => {
      if (auth.isAuthenticated) {
          console.log('Login successful, redirecting to dashboard')
          await router.push('/dashboard')
      } else {
          console.error('Login succeeded but auth state not set')
      }
  }
</script>

<style>
  /* Add your styles here */
  #app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>