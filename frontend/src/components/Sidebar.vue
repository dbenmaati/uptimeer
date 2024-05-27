<template>
	<div class="rg:w-60 flex w-14 flex-shrink-0 flex-col border-r border-gray-300 bg-white" v-if="currentRoute" >
		<div class="flex flex-grow flex-col overflow-y-auto p-2.5">
			<div class="rg:flex hidden flex-shrink-0 items-end text-sm text-gray-600">
				<img src="../assets/insights-logo-new.svg" class="h-7" />
			</div>
			<router-link to="/" class="rg:hidden flex cursor-pointer">
				<img src="../assets/insights-logo-new.svg" class="rounded" />
			</router-link>

			<div class="mt-4 flex flex-col">
				<nav class="flex-1 space-y-1 pb-4 text-base">
					<Tooltip
						v-for="route in sidebarItems"
						:key="route.path"
						placement="right"
						:hoverDelay="0.1"
						class="w-full"
					>
						<template #body>
							<div class="w-fit rounded border border-gray-100 bg-gray-800 px-2 py-1 text-xs text-white shadow-xl" >
								TBD
							</div>
						</template>

						<router-link
							:to="route.path"
							:class="[ route.current
									? 'bg-green-300/100'
									: 'text-gray-700 hover:bg-gray-50 hover:text-gray-800',
								'rg:justify-start group flex w-full items-center justify-center rounded p-2 font-medium',
							]"
							aria-current="page"
						>
							<component
								:is="route.icon"
								:stroke-width="1.5"
								:class="[
									route.current
										? 'text-gray-800'
										: 'text-gray-700 group-hover:text-gray-700',
									'rg:mr-3 rg:h-4 rg:w-4 mr-0 h-5 w-5 flex-shrink-0',
								]"
							/>

							<span class="rg:inline-block hidden">TBD</span>
						</router-link>
					</Tooltip>
				</nav>
			</div>

			
		</div>
	</div>

	
</template>

<script setup>
import { Avatar } from 'frappe-ui'

import { createResource } from 'frappe-ui'
import {
	Book,
	Database,
	GanttChartSquare,
	HomeIcon,
	LayoutPanelTop,
	Settings,
	User,
	Users,
	BookOpen,
} from 'lucide-vue-next'
import { computed, ref, watch } from 'vue'
import { useRoute } from 'vue-router'


const showHelpDialog = ref(false)
const sidebarItems = ref([
	{
		path: '/',
		label: 'Home',
		icon: HomeIcon,
		name: 'Home',
		current: false,
	},
	{
		path: '/dashboard',
		label: 'Dashboards',
		icon: LayoutPanelTop,
		name: 'Dashboard',
		current: false,
	},
	{
		path: '/data-source',
		label: 'Data Sources',
		icon: Database,
		name: 'Data Source',
	},
	{
		path: '/query',
		label: 'Query',
		icon: GanttChartSquare,
		name: 'QueryList',
		current: false,
	},
	{
		path: '/notebook',
		label: 'Notebook',
		icon: Book,
		name: 'Notebook',
		current: false,
	},
	{
		path: '/settings',
		label: 'Settings',
		icon: Settings,
		name: 'Settings',
		current: false,
	},
])

const route = useRoute()
const currentRoute = computed(() => {
	sidebarItems.value.forEach((item) => {
		// check if /<route> or /<route>/<id> is in sidebar item path
		item.current = route.path.match(new RegExp(`^${item.path}(/|$)`))
	})
	return route.path
})

const open = (url) => window.open(url, '_blank')

</script>