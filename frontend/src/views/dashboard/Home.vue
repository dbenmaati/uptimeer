<template>
<div class="flex flex-1 overflow-hidden text-base">
    <Sidebar />
    <div class="flex flex-1 flex-col overflow-hidden">

        <div class="flex flex-1 flex-col space-y-8 overflow-hidden bg-white p-6">
            <div class="space-y-2">
                <div class="text-3xl font-bold text-gray-900">
                    Hello, {{ $store.state.userData.email }} 👋
                </div>
                <div class="text-lg text-gray-600">Wed, 12</div>
            </div>
        </div>
        
    </div>
</div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
import authHeader from '@/stores/modules/auth.header';
import store from '@/stores'

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