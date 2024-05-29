<template>
	<LoginBox class="bg-gray-50" title="Log in to your account">
		<form class="flex flex-col" @submit.prevent="makeLoginRequest">
			<FormControl
				label="Email"
				placeholder="johndoe@mail.com"
				v-model="email"
				name="email"
				autocomplete="email"
				:type="email !== 'Administrator' ? 'email' : 'text'"
				required
			/>

			<FormControl
				class="mt-4"
				label="Username"
				placeholder="Username"
				v-model="inputValue"
				name="Username"
				autocomplete="Username"
				type="text"
				required
			/>

			<FormControl
				class="mt-4"
				label="Password"
				type="password"
				placeholder="•••••"
				v-model="password"
				name="password"
				autocomplete="current-password"
				required
			/>
			<ErrorMessage :error="errorMessage" class="!mt-2" />
			<Button
				class="mt-4"
				variant="solid"
				:disabled="loggingIn"
				:loading="loggingIn"
				@click="makeLoginRequest"
			>
				SignUp
			</Button>
		</form>
	</LoginBox>
</template>

<script setup>
  import { Button, FormControl } from 'frappe-ui'
  import LoginBox from '@/components/LoginBox.vue'

  import { onMounted, ref } from '@vue/runtime-core'

  const loggingIn = ref(null)
  const email = ref(null)
  const password = ref(null)
  const errorMessage = ref(null)
  const redirectRoute = ref(null)
</script>