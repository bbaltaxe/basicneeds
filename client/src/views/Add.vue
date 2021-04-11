<template> 
  <v-card-text>
    <v-container
      fluid
    >
      <v-row>
        <v-col
        cols=3
        >
          <ServiceFilter />
        </v-col>
        <v-col
        cols=9>
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
            <ResourceTable />
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card-text>
</template> 

<script>
  import ServiceFilter from '../components/ServiceFilter.vue'
  import ResourceTable from '../components/ResourceTable.vue'
  export default {
    components: {ServiceFilter,ResourceTable},
    data: () => ({
      sortby: ['Date', 'Location', 'Resource Type', 'Popularity', 'Random'],
      location: ['here']
    }),
  }
</script>

