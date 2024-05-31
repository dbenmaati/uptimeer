<template>
 <Sidebar />
 <h1>HIII, THIS IS TH DASHBOARD</h1>
 <h2> -------- > {{ $store.state.userData.email }}</h2>

</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
import authHeader from '@/stores/modules/auth.header';
import store from '@/stores'
import router from '@/router'

import { onMounted, ref, inject } from 'vue';

const axios = inject('jwtInterceptor');

onMounted(() => {
    axios.get('/auth/user', { headers: authHeader() }).then((response) => {
        store.dispatch('userData/storeUser', {
            username: response.data.user.username,
            email: response.data.user.email
        });
    });
});

</script>