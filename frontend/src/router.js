import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('./views/Login.vue'),
        meta: {
			hideSidebar: true,
		},
    },

    {
        path: '/Signup',
        name: 'Signup',
        component: () => import('./views/Signup.vue'),
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
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
