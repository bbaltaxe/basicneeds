
<template>
  <v-card-text>
    <div class="home">
      <Carousel />
      <v-btn to="/login"
        elevation="2"
      >Login</v-btn>
    </div>
  </v-card-text>
</template>

<script>
  import Carousel from '../components/Carousel.vue'
  export default {
    components:{Carousel}
  };
</script>
