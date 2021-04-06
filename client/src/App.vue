<template>

  <v-app id="inspire">


    <v-main>

      <app-NavBar></app-NavBar>
      <router-view/>
      

    </v-main>
  </v-app>
</template>

<script>
  export default {
    name:'App',
    data () {
      return {

      }
    },
    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>
