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
				label="Password"
				type="password"
				placeholder="•••••"
				v-model="password"
				name="password"
				autocomplete="current-password"
				required
			/>
			<Button
				class="mt-4"
				variant="solid"
				:disabled="loggingIn"
				:loading="loggingIn"
				@click="makeLoginRequest"
			>
				Log in with email
			</Button>
			<br>
			<ErrorMessage :message="errorMessage" style="text-align: center; font-size: 1.2em;" />	
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
	const email = ref(null);
	const password = ref(null);
	const errorMessage = ref(null);

	onMounted(() => {
		if(store.state.authUser.accessToken) (
			router.push({name: 'Dashboard'})
		)
	})

	const makeLoginRequest = async () => {
    if (!email.value || !password.value) {
        errorMessage.value = 'Email and password are required.';
        return;
    }

    try {
        errorMessage.value = null;
        loggingIn.value = true;

        const data = {
            email: email.value,
            password: password.value
        };

        const response = await axios.post('/auth/login', data);

        store.dispatch(
            'authUser/storeToken',
            { access: response.data.access, refresh: response.data.refresh },
            { root: true }
        );

        router.push({ name: 'Dashboard' });

    } catch (error) {
        console.error('Login request failed');
		errorMessage.value = 'Wrong Credentials';
    } finally {
        loggingIn.value = false;
    }
};

</script>