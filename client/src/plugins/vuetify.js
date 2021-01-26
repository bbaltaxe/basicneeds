import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {  
        primary: '#448AFF',
        secondary: '#009688',
        accent: '#00bcd4',
        error: '#3f51b5',
      }
    }
  }
});
