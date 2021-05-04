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
          <span class="headline" v-if="selectedResource">Edit Resource</span>
          <span class="headline" v-else>Add Resource</span>
        </v-card-title>


        <v-card-text>
          <v-text-field
            label="Title*"
            required
            v-model="name"
          />

          <v-textarea
            label="Description*"
            counter
            maxlength="120"
            full-width
            single-line
            required
            v-model="description"
          />

          <v-text-field 
            v-model="hours" 
            label="Hours" 
            hint="Ex: MWF 3pm-5pm, TTh 11am-2pm"
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

          <v-text-field v-model="email" label="Contact Email" />

        </v-card-text>

        <v-card-actions>
          <v-spacer />
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="submitResource"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
  import { bus } from '../main'

  export default {
    data: () => ({
      dialog: false,
      name: "",
      description: "",
      hours: "",
      email: "",
      campuses:['Santa Cruz', 'Los Angeles', 'Merced', 'Riverside', 'Davis', 'San Diego', 'Santa Barbara', 'Berkeley', 'Irvine', 'San Francisco'], 
      options:['Wellness','Food','Housing','Finance','Other'],
      resources:[], 
      locations:[],
      selectedResource: false,
      selectedResourceInfo: Object,
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
        console.log(rawChipValues)
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
        console.log("---compare:---")
        console.log(rawChipValues)
        return rawChipValues
      },
      initForm() {
        //auto fill if editing a resource 
        if (this.selectedResource == true) {
          var selected = this.selectedResourceInfo
          this.name = selected.Name
          this.description = selected.Description;
          this.hours = selected.Hours;
          this.email = selected.Contact;
          this.resources = this.getChipValues(selected.Resource, this.options); 
          this.locations = this.getChipValues(selected.Campus,this.campuses);
        } else {
        
          this.name = "";
          this.description = "";
          this.hours = "";
          this.email = "";
          this.resources = []; 
          this.locations = [];
        }
        
      },
      submitResource(){
        var payload = {
          name: this.name,
          description: this.description,
          hours: this.hours,
          email: this.email,
          campuses: this.selectedChips(this.locations, this.campuses),
          resources: this.selectedChips(this.resources,this.options),
        } 
        //PUSH TO DB HERE
        console.log("_____PAYLOAD_____")
        console.log(payload)
        console.log("_________________")
        this.selectedResource=false;
        this.initForm();
        this.dialog=false;
        return
      },
    }, 
  }
</script>