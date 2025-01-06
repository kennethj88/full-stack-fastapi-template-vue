import { storeToRefs } from 'pinia'

export default defineNuxtRouteMiddleware(async (to,from) => {
  if (import.meta.server) {
    console.log('middleware: server side, skipping auth check')
    return
  }
  const auth = useAuthStore()
  console.log('to:',to,'from:',from)
  //auth.init() 
  console.log('middleware: initted')
  
  // Wait for auth store initialization if needed
  if (!auth.initialized) {
    console.log('auth middelware: auth not initialized')
    await auth.init()
    await new Promise(resolve => setTimeout(resolve, 100))
  }
  
  console.log('Middleware check:', {
      isAuthenticated: auth.isAuthenticated,
      currentPath: to.path,
      //hydrated: auth.$state.hydrated,
      email: auth.user?.email
  })
    
    //if (import.meta.client) {
    //  await until(() => auth.hydrated === true)
    // }

  // Public routes that don't require authentication
  const publicRoutes = [
    '/login', 
    '/signup', 
    '/recover-password',
    '/reset-password'
  ]
 
  
  // Allow access to reset-password with token
  if (to.path.startsWith('/reset-password/')) {
    return
  }
  console.log('Redirecting to login - not authenticated',!auth.isAuthenticated,!publicRoutes.includes(to.path), to.path)

  if (!auth.isAuthenticated && !publicRoutes.includes(to.path)) {
    console.log('Redirecting to login - NOT  authenticated')
    
    return navigateTo('/login')
  }

  if (auth.isAuthenticated && publicRoutes.includes(to.path)) {
    console.log('Redirecting to dashboard - already authenticated')
    return navigateTo('/dashboard')
  }
}) 