<template>
    <forgotPasswordForm
       :onSuccess="onSuccess"
     />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Component } from 'vue'
import ForgotPasswordForm from '@/components/auth/ForgotPasswordForm.vue'
import { useRouter } from 'vue-router'
import { useToast } from '@/composables/useToast'

const router = useRouter()
const { showToast } = useToast()

const onSuccess = async () => {
  showToast({
    message: 'Password reset instructions have been sent to your email',
    type: 'success'
  })
  await router.push('/login')
}

</script>

<style scoped>
/* Add your styles here */
</style>
 
