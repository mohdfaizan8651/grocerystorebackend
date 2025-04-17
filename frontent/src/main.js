// import './assets/main.css'

import { createApp, setDevtoolsHook } from "vue";
import App from "./App.vue";
import router from "./router";
import Vuecookies from "vue-cookies";
import { createStore } from "vuex";
// import { Store } from 'vuex/types/index.js';

const app = createApp(App);

app.use(router);
app.use(Vuecookies);

const store = createStore({
  state: {
    role: sessionStorage.getItem("role"),
    loggedIn: sessionStorage.getItem("loggedIn"),
  },
  mutations: {
    setRole(state, role) {
      state.role = role;
    },
    setLogin(state) {
      state.loggedIn = true;
    },
    logout(state) {
      state.role = null;
      state.loggedIn = false;
    },
  },
});

export default store;
app.use(store);

app.mount("#app");
