import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        isAuth: true,
    },
    mutations: {
        authorizationComplete(state, value) {
            state.isAuth = value;
        },
    },
    // actions: {
    //     // registry(payload) {
    //     //
    //     // },
    // }
})