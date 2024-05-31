export default {
    namespaced: true,
    state: {
        user: {
            username: null,
            email: null,
        }
    },
    mutations: {
        storeUser(state, { username, email }) {
            state.username = username
            state.email = email
        }
    },
    actions: {
        storeUser({commit}, { username, email }) {
            commit('storeUser', { username, email })
        },
    },
    getters: {
        fullName(state) {
            return state.user.username
        }
    }
}