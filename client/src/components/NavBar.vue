<template>
  <div id="app">
    <v-app id="inspire">
      <v-card>
        <v-toolbar
          color="blue"
          dark
          flat
        >

          <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
          <v-toolbar-title style="cursor: pointer" @click="$router.push('/')">Basic Needs</v-toolbar-title>

          <v-spacer>

          </v-spacer>

          <v-btn icon>
            <v-icon>mdi-magnify</v-icon>
          </v-btn>

          <v-btn icon to="/homePage">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>

          <template v-slot:extension>
            <v-tabs
              v-model="model"
              centered
              slider-color="white"
            >

              <app-Login></app-Login>

              <v-tab to="/housing"
              >
                Housing
              </v-tab>
              <v-tab
              >
                Financial
              </v-tab>
              <v-tab to="/groceries"
              >
                Food
              </v-tab>
              <v-tab to="/mental_wellbeing"
              >
                Wellbeing
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
