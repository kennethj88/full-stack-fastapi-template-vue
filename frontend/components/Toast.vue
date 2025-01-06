<template>
  <div class="toast toast-end">
    <div v-if="isVisible" :class="[
      'alert',
      type === 'success' ? 'alert-success' : 
      type === 'error' ? 'alert-error' : 'alert-info'
    ]">
      {{ message }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { useToast } from '~/composables/useToast'

const { isVisible, message, type } = useToast()
</script> 