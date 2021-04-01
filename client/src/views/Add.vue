<template> 
  <v-card-text>
    <div class="container-fluid">
      
      <div class="row">
        <div class="col-xs">
          <ServiceFilter />
        </div>
        <div class="col">
          <v-card 
            color="grey"
            class="mx-auto"
          > 
            <v-col
              class="d-flex"
              cols="12"
              sm="6"
            >
              <v-select
                :items="sortby"
                label="Sort By"
                solo
              />

            </v-col>

            Resources can go here
            <v-card> 
            Maybe in their own card
          </v-card>

          or something

    

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

