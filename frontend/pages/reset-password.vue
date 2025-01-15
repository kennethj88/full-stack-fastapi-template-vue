<template>
  <div class="container">
    <ResetPasswordForm />
  </div>
</template>

<script setup lang="ts">
import ResetPasswordForm from '~/components/auth/ResetPasswordForm.vue'

definePageMeta({
  middleware: ['auth']
})
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
</style> 