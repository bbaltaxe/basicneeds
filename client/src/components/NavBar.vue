<template> 
  <div>
    <v-navigation-drawer
      v-model="drawer"
      absolute
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
      app
      color="primary"
    >
      <v-app-bar-nav-icon @click="drawer = !drawer" />
      <v-toolbar-title
        style="cursor: pointer"
        @click="$router.push('/')"
      >
        UC-Wide Basic Needs
      </v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>



  export default {
    components:{
    },
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
    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>