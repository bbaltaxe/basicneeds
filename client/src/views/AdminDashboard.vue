<template> 
  <v-card-text>
    <!-- TOOLBAR --> 
    <v-container
      fluid
    >
      <v-toolbar
        color="primary"
        dark
        flat
      >
        <v-toolbar-title>Admin Dashboard</v-toolbar-title>
        <template v-slot:extension>
          <v-tabs
            v-model="tab"
            align-with-title
          >
            <v-tabs-slider color="white" />

            <v-tab>Resources</v-tab>
            <v-tab>Announcements</v-tab>
          </v-tabs>
        </template>
      </v-toolbar>


      <v-tabs-items v-model="tab">
        <!-- RESOURCE EDIT PAGE -->
        <v-tab-item>
          <v-card>
            <v-card-text>Edit resource information here</v-card-text>
          </v-card>

          <v-card
            class="mx-auto"
            flat
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
                <v-btn
                  elevation="2"
                  color="green"
                >
                  add 
                </v-btn>
                <v-btn
                  elevation="2"
                  color="orange"
                >
                  edit
                </v-btn>
                <v-btn
                  elevation="2"
                  color="red"
                >
                  remove
                </v-btn>
                <v-card 
                  color="grey"
                  class="mx-auto"
                > 
                  <SortBar />
                  <ResourceTable />
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-tab-item>

        <!-- ANNOUNCEMENT EDIT PAGE -->
        <v-tab-item>
          <v-card>
            <v-card-text>Edit announcement information here</v-card-text>
          </v-card>
          <v-card
            class="mx-auto"
            flat
          > 
            <v-row>
              <v-col
                cols="9"
              >
                <v-btn
                  elevation="2"
                  color="green"
                >
                  <AnnounceForm />
                </v-btn>
                <v-btn
                  elevation="2"
                  color="orange"
                  dark
                >
                  edit
                </v-btn>
                <v-btn
                  elevation="2"
                  color="red"
                  dark
                >
                  remove
                </v-btn>
                <v-card 
                  color="grey"
                  class="mx-auto"
                  flat 
                  dark
                > 
                  <v-card-text> announcement content can go here </v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </v-card-text>
</template> 

<script>
  import ServiceFilter from '../components/ServiceFilter.vue'
  import ResourceTable from '../components/ResourceTable.vue'
  import SortBar from '../components/SortBar.vue'
  import AnnounceForm from '../components/AnnounceForm.vue'
  export default {
    components: {ServiceFilter,ResourceTable,SortBar,AnnounceForm},
    data () {
      return {
        tab: null,
      }
    },
  }
</script>
