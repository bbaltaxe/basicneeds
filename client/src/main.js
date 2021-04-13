import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';

import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import NavBar from './components/NavBar.vue'
import Login from './components/Login.vue'
import HomePage from './components/HomePage.vue'
import Intake from './components/Intake.vue'
import Popup from './components/Popup.vue'
import AddResource from './components/AddResource.vue'

Vue.config.productionTip


Vue.component('app-NavBar',NavBar);
Vue.component('app-Login',Login);
Vue.component('app-HomePage',HomePage);
Vue.component('app-Intake',Intake);
Vue.component('app-Popup',Popup);
Vue.component('app-Add',AddResource);

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

new Vue({
  el: '#app',
  vuetify: new Vuetify(),
  data () {
    return {
      items: [
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
        },
        {
          src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
        },
      ],
    }
  },
})
