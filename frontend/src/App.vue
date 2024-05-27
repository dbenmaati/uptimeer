<!-- src/App.vue -->
<template>
  <div class="flex h-screen w-screen bg-white antialiased">
		<div class="flex flex-1 overflow-hidden text-base">
		  <RouterView v-slot="{ Component }"></RouterView>
	  </div>
	</div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
import { computed, inject, onBeforeUnmount } from 'vue'
import { useRoute } from 'vue-router'
import { Toaster } from 'vue-sonner'

const route = useRoute()
const isGuestView = computed(() => route.meta.isGuestView)
const hideSidebar = computed(() => route.meta.hideSidebar)

</script>
