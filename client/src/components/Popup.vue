<div id="app">
  <v-app id="inspire">
    <v-row
      align="center"
      justify="center"
    >
      <v-card
        height="300"
        width="250"
      >
        <v-row justify="center">
          <v-btn
            color="success"
            class="mt-12"
            @click="overlay = !overlay"
          >
            Login
          </v-btn>

          <v-overlay
            :absolute="absolute"
            :value="overlay"
          >
            <v-btn
              color="success"
              @click="overlay = false"
            >
              Continue
            </v-btn>
          </v-overlay>
        </v-row>
      </v-card>
    </v-row>
  </v-app>
</div>
new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  data: () => ({
    absolute: true,
    overlay: false,
  }),
})
