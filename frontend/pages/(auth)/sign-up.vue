<template>
     <signupForm
        @signup-success="onSuccess"
      />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import signupForm from '@/components/auth/SignupForm.vue'

const router = useRouter()

const onSuccess = async () => {
    console.log('on success')
    await router.push('/dashboard') // Redirect after successful login
}

</script>

<style scoped>
/* Add your styles here */
</style>
  
