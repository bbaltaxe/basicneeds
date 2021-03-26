import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import NavBar from './components/NavBar.vue'
import Login from './components/Login.vue'
import HomePage from './components/HomePage.vue'
import Intake from './components/Intake.vue'
import Popup from './components/Popup.vue'

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

Vue.component('app-NavBar',NavBar);
Vue.component('app-Login',Login);
Vue.component('app-HomePage',HomePage);
Vue.component('app-Intake',Intake);
Vue.component('app-Popup',Popup);
