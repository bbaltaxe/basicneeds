<template>
  <div>
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="green"
          dark
          elevation="0"
          v-bind="attrs"
          v-on="on"
        >
          Add
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span
            v-if="selectedAnnouncement"
            class="headline"
          >Edit Announcement</span>
          <span
            v-else
            class="headline"
          >Add Announcement</span>
        </v-card-title>
      
        <v-tabs-items v-model="tab">
          <v-tab-item>
            <!------------- FORM ---------------->

            <v-card-text>
              <v-text-field
                v-model="title"
                label="Title*"
                required
              />

              <v-textarea
                v-model="description"
                label="Description*"
                counter
                maxlength="120"
                full-width
                single-line
                required
              />

              <v-row>
                <v-col
                  cols="12"
                  lg="6"
                >
                  <v-text-field
                    v-model="urlLink"
                    label="Url to image"
                  />
                </v-col>
                <v-col
                  cols="12"
                  lg="6"
                >
                  <v-text-field
                    v-model="altText"
                    label="Alt text for image"
                  />
                </v-col>
              </v-row>


              <v-row>
                <v-col
                  cols="12"
                  lg="6"
                >
                  <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="date"
                        label="Post Date*"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      />
                    </template>
                    <v-date-picker
                      v-model="date"
                      no-title
                      scrollable
                    >
                      <v-spacer />
                      <v-btn
                        text
                        color="primary"
                        @click="menu = false"
                      >
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(date)"
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>

                <v-col
                  cols="12"
                  lg="6"
                >
                  <v-menu
                    ref="menu2"
                    v-model="menu2"
                    :close-on-content-click="false"
                    :return-value.sync="date2"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="date2"
                        label="Remove Date*"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      />
                    </template>
                    <v-date-picker
                      v-model="date2"
                      no-title
                      scrollable
                    >
                      <v-spacer />
                      <v-btn
                        text
                        color="primary"
                        @click="menu2 = false"
                      >
                        Cancel
                      </v-btn>
                      <v-btn
                        text
                        color="primary"
                        @click="$refs.menu2.save(date2)"
                      >
                        OK
                      </v-btn>
                    </v-date-picker>
                  </v-menu>
                </v-col>
              </v-row>

              <v-card-text>
                Relevant Resources*

                <v-chip-group
                  v-model="resources"
                  column
                  multiple
                >
                  <v-chip
                    v-for="option in options"
                    :key="option"
                    filter 
                    outlined
                  > 
                    {{ option }}
                  </v-chip>
                </v-chip-group>
              </v-card-text>

              <v-card-text>
                Relevant Campuses*
                <v-chip-group
                  v-model="locations"
                  column
                  multiple
                >
                  <v-chip
                    v-for="campus in campuses"
                    :key="campus"
                    filter 
                    outlined
                  > 
                    {{ campus }}
                  </v-chip>
                </v-chip-group>
              </v-card-text>

              <v-btn 
                block
                color="error"
                dark
                @click="tab = 2"
              >
              Remove
              </v-btn>
            </v-card-text>



            <v-card-actions>
              <v-spacer />
              <v-btn
                color="blue darken-1"
                text
                @click="dialog = false && initForm"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="tab = 1"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-tab-item>

          <v-tab-item>
            <!------------- CHECK ---------------->
            <v-card-text><h3>This is what your resource will look like:</h3></v-card-text>
        
            <Announcement 
              :info="getPayload()"
            />
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="blue darken-1"
                text
                @click="dialog = false && initForm"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="tab = 0"
              >
                Edit
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="submitAnnouncement()"
              >
                Submit
              </v-btn>
            </v-card-actions>
          </v-tab-item>

          <v-tab-item>
            <!------------- CHECK on Remove ---------------->
            <v-card-text><h3>Are you sure you want to permanently remove this announcement?</h3></v-card-text>
            <Announcement 
              :info="getPayload()"
            />
            <v-card-actions>
              <v-spacer />
              <v-btn
                color="blue darken-1"
                text
                @click="dialog = false && initForm"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="removeResource()"
              >
                Remove
              </v-btn>
            </v-card-actions>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
  import { bus } from '../main'
  import Announcement from './Announcement.vue'
  export default {
    components: {Announcement},
    data: () => ({
      //popup control
      dialog: false,
      menu: false,
      menu2: false,

      //payload
      date: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      resources:[], 
      locations:[],
      title: "",
      description:"",
      urlLink:"",
      altText:"",

      //data for populating chips
      campuses:['Santa Cruz', 'Los Angeles', 'Merced', 'Riverside', 'Davis', 'San Diego', 'Santa Barbara', 'Berkeley', 'Irvine', 'San Francisco'], 
      options:['Wellness','Food','Housing','Finance','Other'],

      //data for editing resources
      selectedAnnouncement: false,
      selectedAnnouncementInfo: Object,

      //data for check screen
      tab:0,
    }),
    created (){
      bus.$on('editAnnouncement', (data) => {
        this.selectedAnnouncementInfo = data;
        this.selectedAnnouncement = true;
        this.initForm();
        this.dialog = true
      })
    }, 
    methods: {
      selectedChips(rawChipValues,nameList){
        var value = Object.values(rawChipValues);
        var selected = []
        value.sort()
        //matching values to locations
        for(var i=0; i<value.length; i++){
          selected.push(nameList[value[i]])

        }

        return selected

      },
      getChipValues(selected,nameList){
        var rawChipValues = []
        for (var i=0; i<selected.length; i++){

          rawChipValues.push(nameList.indexOf(selected[i]));

        }
        return rawChipValues
      },
      initForm() {
        //auto fill if editing a resource 
        this.tab = 0;
        if (this.selectedAnnouncement == true) {
          var selected = this.selectedAnnouncementInfo
          this.urlLink = selected.Image;
          this.altText = selected.AltText;
          this.title = selected.Title;
          this.description = selected.Description;
          this.resources = this.getChipValues(selected.Resource, this.options); 
          this.locations = this.getChipValues(selected.Campus,this.campuses);
          this.date = this.postDate; 
          this.date2 = this.removeDate;
          
        } else {
        
          this.urlLink = '';
          this.altText = '';
          this.title = '';
          this.description = '';
          this.resources = []; 
          this.locations = [];
          //this.date = this.postDate; 
          //this.date2 = this.removeDate;
        }
        
      },
      getPayload(){
        console.log(this.date)
        var payload = {
          Title: this.title,
          Description: this.description,
          Image: this.urlLink,
          AltText: this.altText,
          Campus: this.selectedChips(this.locations,this.campuses),
          Resource: this.selectedChips(this.resources,this.options),
          PostDate: this.date,
          RemoveDate: this.date2,
        }
        return payload
      },
      submitAnnouncement(){

        //JESSY YOU CAN ADD DB STUFF HERE 
        // post getPayload()


        this.selectedAnnouncement=false;
        this.initForm();
        this.dialog=false;

        //on success: 
        bus.$emit('submissionAlert',"Successfully added Announcement")
        //on fail
        //bus.$emit('submissionAlert',"An error occurred, please try again later.")

      },
      removeResource(){
        //JESSY YOU CAN ADD DB STUFF HERE 
        // remove getPayload()

        this.selectedResource=false;
        this.initForm();
        this.dialog=false;
        //on success: 
        bus.$emit('submissionAlert',"Announcement has been removed")
        //on fail
        //bus.$emit('submissionAlert',"An error occurred, please try again later.")
      },
    },
    
  }
</script>