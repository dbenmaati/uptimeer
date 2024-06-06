<template>
<div class="flex flex-1 overflow-hidden text-base">
    <Sidebar />
	<div class="flex flex-1 flex-col overflow-hidden">
        
        <header class="sticky top-0 z-10 flex items-center justify-between bg-white px-5 py-2.5">
            <PageBreadcrumbs class="h-7" :items="[{ label: 'Dashboards' }]" />
            <div class="space-x-2.5">
                <Button label="New Dashboard" variant="solid" @click="showDialog = true">
                    <template #prefix>
                        <Plus class="h-4 w-4" />
                    </template>
                </Button>
            </div>
        </header>

        <div class="flex flex-1 space-y-4 overflow-hidden bg-white px-5 py-2">
            <div v-if="dashboards?.list?.length" class="flex flex-1 flex-col space-y-6 overflow-y-auto p-1">
                <DashboardsGroup
                    v-if="favorites.length > 0"
                    :dashboards="favorites"
                    title="Favorites"
                />
                <DashboardsGroup
                    v-if="settings.enable_permissions"
                    :dashboards="privates"
                    title="Private"
                />
                <DashboardsGroup :dashboards="sortedDashboards" title="All" :enableSearch="true" />
            </div>
            <div v-else class="flex flex-1 flex-col items-center justify-center space-y-1">
                <div class="text-base font-light text-gray-600">
                    You haven't created any dashboards yet.
                </div>
                <div
                    class="cursor-pointer text-sm font-light text-blue-500 hover:underline"
                    @click="showDialog = true"
                >
                    Create a new dashboard
                </div>
            </div>
        </div>

        <Dialog :options="{ title: 'New Dashboard' }" v-model="showDialog">
            <template #body-content>
                <Input
                    type="text"
                    label="Title"
                    placeholder="Enter a suitable title..."
                    v-model="newDashboardTitle"
                />
            </template>
            <template #actions>
                <Button
                    class="w-full"
                    variant="solid"
                    @click="createDashboard"
                >
                    Create
                </Button>
            </template>
	    </Dialog>

        
    </div>
</div>
</template>

<script setup>

// BASE IMPORT
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
// END BASE IMPORT


import PageBreadcrumbs from '@/components/PageBreadcrumbs.vue'
import { Plus } from 'lucide-vue-next'
import { useRoute, useRouter } from 'vue-router'
import { Button, Input, Dialog} from 'frappe-ui';


const showDialog = ref(false)
const route = useRoute()
if (route.hash == '#new') {
	showDialog.value = true
}

const newDashboardTitle = ref('')
const router = useRouter()

async function createDashboard() {
	const name = await dashboards.create(newDashboardTitle.value)
	showDialog.value = false
	newDashboardTitle.value = ''
	router.push(`/dashboard/${name}`)
}
</script>