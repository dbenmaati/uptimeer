<template>
	<LoginBox class="bg-gray-50" title="Log in to your account">
		<form class="flex flex-col" @submit.prevent="makeLoginRequest">
			<FormControl
				label="Full Name"
				placeholder="Full Name"
				v-model="full_name"
				name="Full Name"
				autocomplete="Full Name"
				type="text"
				required
			/>
			
			<FormControl
			class="mt-4"
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
				label="Password"
				type="password"
				placeholder="•••••"
				v-model="password"
				name="password"
				autocomplete="current-password"
				required
			/>

			<FormControl
				class="mt-4"
				label="Password verification"
				type="password"
				placeholder="•••••"
				v-model="password2"
				name="Password verification"
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
			<br>
			<ErrorMessage :message="errorMessage" style="text-align: center; font-size: 1em;" />	
		</form>
	</LoginBox>
</template>

<script setup>

	import LoginBox from '@/components/LoginBox.vue';

	import { Button, FormControl, ErrorMessage } from 'frappe-ui';
	import { onMounted, ref, inject } from 'vue';

	import store from '@/stores'
	import router from '@/router'

	const axios = inject('jwtInterceptor');

	const loggingIn = ref(null);
	const full_name = ref(null);
	const email = ref(null);
	const password = ref(null);
	const password2 = ref(null);
	const errorMessage = ref(null);

	onMounted(() => {
		if(store.state.authUser.accessToken) (
			router.push({name: 'Dashboard'})
		)
	})

	const makeLoginRequest = async () => {
		
		if (!full_name.value || !email.value || !password.value || !password2.value) {
			errorMessage.value = 'Pleas fill all form.';
			return;
    	}

		if (password.value != password2.value) {
			errorMessage.value = 'Please double check your password';
			return;
    	}

		try {
			errorMessage.value = null;
			loggingIn.value = true;
		
			const data = {
				full_name: full_name.value,
				email: email.value,
				password: password.value,
				password2: password2.value
			};

			const response = await axios.post('/auth/register', data);

			router.push({ name: 'Login' });

		} catch (error) {
			errorMessage.value = 'Unknown Error';
		} finally {
			loggingIn.value = false;
		}
	};

</script>