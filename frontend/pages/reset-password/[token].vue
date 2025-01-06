<template>
  <div class="container">
    <ResetPasswordForm :token="token" />
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const token = route.params.token as string

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