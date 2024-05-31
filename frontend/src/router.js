import { createRouter, createWebHistory } from 'vue-router'
import authStore from "@/stores/modules/auth.store"


const routes = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('./views/Login.vue'),
    },

    {
        path: '/register',
        name: 'Register',
        component: () => import('./views/Register.vue'),
    },

    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('./views/dashboard/Dashboard.vue'),
        meta: {
            requiresAuth: true,
        }
    },

    {
        path: '/dashboard/sites',
        name: 'Sites',
        component: () => import('./views/dashboard/Sites.vue'),
    },

    // otherwise redirect to 404 //
    {
        path: '/page-not-found',
        name: 'page-not-found',
        component: () => import('./views/404-error.vue'),
    },
    
    {
        path: '/:pathMatch(.*)*',
        redirect: '/page-not-found' 
    },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {

    const requiresAuth = to.matched.some(record  => record.meta.requiresAuth)
    const isActive = authStore.state.accessToken
  
    if (requiresAuth && !isActive) {
        next('/login')
    } 
    else if (requiresAuth && isActive) {
        next()
    } 
    else {
        next()
    }
  
})

export default router
