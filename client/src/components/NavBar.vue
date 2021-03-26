<template>
  <div id="app">
    <v-app id="inspire">
      <v-card>
        <v-toolbar
          color="blue"
          dark
          flat
        >
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
          <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title style="cursor: pointer" @click="$router.push('/')">Basic Needs</v-toolbar-title>

          <v-spacer>
          </v-spacer>

          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>

          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>

          <template v-slot:extension>
            <v-tabs
              v-model="model"
              centered
              slider-color="white"
            >

              <app-Login></app-Login>

              <v-tab
              >
                Housing
              </v-tab>
              <v-tab
              >
                Financial
              </v-tab>
              <v-tab
              >
                Food
              </v-tab>

            </v-tabs>
          </template>
        </v-toolbar>

        <v-tabs-items v-model="model">
          <v-tab-item
            v-for="i in 3"
            :key="i"
            :value="`tab-${i}`"
          >
            <v-card flat>
              <v-card-text v-text="text"></v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
    </v-app>
  </div>
</template>


<script>
  export default {
    name:'NavBar',
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

/*
new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  data () {
    return {
      model: 'tab-2',
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },
})
*/
</script>