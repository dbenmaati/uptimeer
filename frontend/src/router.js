import { createRouter, createWebHistory } from 'vue-router'


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
})

export default router
