<template>
  <v-app id="inspire">
    
    <v-main> 
      
        <router-view/>

    

<v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
        >
          <v-list-item to="/groceries">
            <v-list-item-title>Groceries</v-list-item-title>
          </v-list-item>

          <v-list-item to="/mental_wellbeing">
            <v-list-item-title>Mental Wellbeing</v-list-item-title>
          </v-list-item>

          <v-list-item to="/housing">
            <v-list-item-title>Housing</v-list-item-title>
          </v-list-item>

          <v-list-item to="/about">
            <v-list-item-title>About</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar 
    app color=primary>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title style="cursor: pointer" @click="$router.push('/')">Basic Needs</v-toolbar-title>

    </v-app-bar>

   </v-main>
  </v-app>
</template>

<script>


  export default {
    name:'App',
    data () {
      return {
        drawer: false,
        group: null,
        colors: [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ],
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
      }
    },
    components:{
    
    },
    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>
