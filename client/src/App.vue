<template>
  <v-app id="inspire">
    <v-main>
      <router-view />
      <navBar />
    </v-main>
  </v-app>
</template>

<script>

  import navBar from "./components/NavBar.vue"

  export default {
    name:'App',
    components:{
      navBar,
    },
    data () {
      return {
        
      }
    },
  }
</script>
