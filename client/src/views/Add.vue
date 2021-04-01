<template> 
  <v-card-text>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm">
          <ServiceFilter/>
        </div>
      <div class="col-lg">
    
      <v-card 
      class = "mr-auto"> 
      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-select
          :items="sortby"
          label="Sort By"
          solo
        ></v-select>
      </v-col>
    </v-card>
  </div>
    </div>
    </div>
  </v-card-text>
</template> 

<script>
  import ServiceFilter from '../components/ServiceFilter.vue'
  export default {
    components: {ServiceFilter},
    data: () => ({
      sortby: ['Date', 'Location', 'Resource Type', 'Popularity', 'Random'],
      location: ['here']
    }),
  }
</script>

