<template> 
  <v-card-text>
    <v-container
      fluid
    >
      <v-row>
        <v-col
          cols="3"
        >
          <ServiceFilter />
        </v-col>
        <v-col
          cols="9"
        >
          <v-card 
            color="grey"
            class="mx-auto"
          > 
            <SortBar />
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
  import SortBar from '../components/SortBar.vue'
  export default {
  components: {ServiceFilter,ResourceTable,SortBar},
  }
</script>

