<template>
  <v-app id="inspire">
    <v-main>
      <router-view />
      <navBar />
    </v-main>
  </v-app>
</template>

<script>
import navBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    navBar,
  },
  data() {
    return {
      isAuthenticated: this.$session.exists(),
      username: this.$session.get("username"),
    };
  },
  methods: {
    logout() {
      if (this.isAuthenticated) {
        this.$session.destroy();
        this.isAuthenticated = false;
      } else {
        this.$router.push(`/login`);
      }
    },
  },
};
</script>
