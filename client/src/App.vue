<template>

  <v-app id="inspire">


    <v-main>
      <div>
        <app-NavBar/>
      </div>
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
