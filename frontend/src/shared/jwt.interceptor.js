import Axios from 'axios'
import store from '@/stores/index'
import router from '@/router'

let baseURL = 'http://127.0.0.1:8000/api'

const jwtInterceptor = Axios.create({
    baseURL: baseURL,
    //withCredentials: true,
  });

// create interceptor for acess token and refresh
jwtInterceptor.interceptors.request.use((config) => {
  return config
})

jwtInterceptor.interceptors.response.use(
  
    (response) => {
        return response
    },

    async (error) => {

        if (error.response.status === 401) {

            var data = {
                refresh: store.state.authUser.refreshToken
            }

            Axios.post(baseURL + '/auth/refresh', data).then((response) => {

                store.dispatch(
                    'authUser/refreshToken',
                    {access: response.data.access}
                )

            }).catch(() => {
                //return Promise.reject(err);
                store.dispatch('authUser/logoutUser')
                router.push({name: 'Login'})
            });

        } else {
            return Promise.reject(error);
            //store.dispatch('authUser/logoutUser')
        }
    }
)

export default jwtInterceptor;