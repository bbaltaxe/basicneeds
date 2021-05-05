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
            v-if="selectedResource"
            class="headline"
          >Edit Resource</span>
          <span
            v-else
            class="headline"
          >Add Resource</span>
        </v-card-title>


        <v-tabs-items v-model="tab">
          <v-tab-item>
            <!------------- FORM ---------------->
            <v-card-text>
              <v-text-field
                v-model="name"
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

              <v-text-field 
                v-model="hours" 
                label="Hours" 
                hint="Ex: MWF 3pm-5pm, TTh 11am-2pm"
                required 
              />

              <v-text-field 
                v-model="address" 
                label="Location" 
                hint="Ex: Student Health Center, Room 112"
                required 
              />

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

              <v-text-field
                v-model="email"
                label="Contact Email"
              />
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
            <ListItem :info="getPayload()" />
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
                @click="submitResource()"
              >
                Submit
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
  import ListItem from './ListItem.vue'

  export default {
    components: {ListItem},
    data: () => ({
      //popup control
      dialog: false,

      //payload
      name: "",
      description: "",
      hours: "",
      email: "",
      resources:[], 
      locations:[],
      address: "",

      //data for populating chips
      campuses:['Santa Cruz', 'Los Angeles', 'Merced', 'Riverside', 'Davis', 'San Diego', 'Santa Barbara', 'Berkeley', 'Irvine', 'San Francisco'], 
      options:['Wellness','Food','Housing','Finance','Other'],

      //data for editing resources
      selectedResource: false,
      selectedResourceInfo: Object,

      //data for check screen
      tab:0,
    }),
    created (){
      bus.$on('editResource', (data) => {
        this.selectedResourceInfo = data;
        this.selectedResource = true;
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
        if (this.selectedResource == true) {
          var selected = this.selectedResourceInfo
          this.name = selected.Name
          this.description = selected.Description;
          this.hours = selected.Hours;
          this.email = selected.Contact;
          this.resources = this.getChipValues(selected.Resource, this.options); 
          this.locations = this.getChipValues(selected.Campus,this.campuses);
          this.address = selected.Location;
        } else {
        
          this.name = "";
          this.description = "";
          this.hours = "";
          this.email = "";
          this.resources = []; 
          this.locations = [];
          this.address = [];
        }
        
      },
      getPayload(){
         var payload = {
          Campus: this.selectedChips(this.locations, this.campuses),
          Location: this.address,
          Resource: this.selectedChips(this.resources,this.options),
          Name: this.name,
          Description: this.description,
          Hours: this.hours,
          Contact: this.email,
        }
        return payload
      },
      submitResource(){

        //JESSY YOU CAN ADD DB STUFF HERE 
        // post getPayload()


        this.selectedResource=false;
        this.initForm();
        this.dialog=false;

        //on success: 
        bus.$emit('submissionAlert',"Successfully added Resource")
        //on fail
        //bus.$emit('submissionAlert',"An error occurred, please try again later.")

      }
    }, 
  }
</script>