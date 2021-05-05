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
                  <ResourceForm/>
                </v-btn>
                <v-btn
                  elevation="2"
                  color="orange"
                  @click="enableEditResource"
                >
                  edit / remove
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
                  <AnnounceForm/>
                </v-btn>
                <v-btn
                  elevation="2"
                  color="orange"
                  @click="enableEditAnnouncement"
                >
                  edit / remove
                </v-btn>
                <v-card 
                  color="grey"
                  class="mx-auto"
                  flat 
                > 
                  <SortBar />
                  <AnnouncementTable />

                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-container>

    <!--show submission announcements-->
    <v-snackbar
      v-model="snackbar"
      color="primary"
    >
      {{snackText}}
    </v-snackbar>

  </v-card-text>
</template> 

<script>

import axios from "axios";
  import { bus } from '../main'
  import ServiceFilter from '../components/ServiceFilter.vue'
  import ResourceTable from '../components/ResourceTable.vue'
  import AnnouncementTable from '../components/AnnouncementTable.vue'
  import SortBar from '../components/SortBar.vue'
  import AnnounceForm from '../components/AnnounceForm.vue'
  import ResourceForm from '../components/ResourceForm.vue'

  export default {
    components: {ServiceFilter,ResourceTable,AnnouncementTable,SortBar,AnnounceForm,ResourceForm},
    data () {
      return {
        tab: null,
        editResource: false,
        editAnnouncement:false, 

        //success/fail alert
        snackbar:false,
        snackText:"",
      }
    },
    methods: {
      enableEditResource(){
        if(this.editResource == false){
          this.editResource = true
        }
        else {
          this.editResource = false
        }
        bus.$emit('enableEditResource',this.editResource)
      },
      enableEditAnnouncement(){
        if(this.editAnnouncement == false){
          this.editAnnouncement = true
        }
        else {
          this.editAnnouncement = false
        }
        bus.$emit('enableEditAnnouncement',this.editAnnouncement)
      },
    },
    created (){
      //show snackbar
      bus.$on('submissionAlert', (data) => {
        this.snackText=data; 
        this.snackbar=true;
      })
    },

  }
</script>
