<template>
  <div id="app">
    <v-row justify="space-around">
      <v-icon @click="model--">
        mdi-minus
      </v-icon>
      {{ model }}
      <v-icon @click="model++">
        mdi-plus
      </v-icon>
    </v-row>
    <v-carousel v-model="model">
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        >
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        colors: [
          'primary',
          'secondary',
          'yellow darken-2',
          'red',
          'orange',
        ],
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
        model: 0,
      }
    },
  }
</script>
