import Vue from "vue";
import api from "@/services/api";

const authStore = new Vue({
  data() {
    return {
      user: {},
    };
  },
  computed: {
    isUserLogged() {
      return Object.keys(this.user).length != 0;
    },
  },
  methods: {
    async login(loginData) {
      const user = await api.auth.login(loginData);
      this.user = user;
    },
    logout() {
      api.authToken = null;
      this.user = {};
    },
  },
});

Vue.prototype.$auth = authStore;

export default authStore;
