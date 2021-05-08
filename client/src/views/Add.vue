<template>
  <v-card-text>
    <v-container
      fluid
    >
      <v-row>
        <v-col
          cols="3"
        >
          <dashSideBar/>
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
            <ServiceFilter />
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
  import dashSideBar from '../components/dashSideBar.vue'
  export default {
  components: {ServiceFilter,ResourceTable,SortBar,dashSideBar},
  }
</script>
