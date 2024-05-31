import { createApp } from 'vue'
import './index.css'
import App from './App.vue'
import router from './router'

import store from '@/stores'
import jwtInterceptor from '@/shared/jwt.interceptor'

const app = createApp(App)

app.use(store)
app.use(router)

// INTERCEPTO TO VALIDATE ALL REQUESTS - SHOULD BE INCLUDED IN COMPONENT TO BE USED
// app.config.globalProperties.$axios = {...jwtInterceptor}  
// -> OLD VERSION WITOUT INCLUDE IN COMP BUT SHOULD NOT USED IN <script setup>
app.provide('jwtInterceptor', jwtInterceptor)

app.mount('#app')
