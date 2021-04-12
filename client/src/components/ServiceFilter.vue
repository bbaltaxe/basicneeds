<template>
  <v-container
    fluid
  >
    <v-card
      class="mr-auto"
      max-width="300"
    >
      <v-toolbar
        flat
        color="grey accent-4"
        dark
      >
        <v-toolbar-title>Filter Results</v-toolbar-title>
      </v-toolbar>

      <!-- RESOURCE GROUP --> 

      <v-card-text>
        <h2 class="title mb-2">
          Resource Type
        </h2>

        <v-switch
          v-model="ractive"
          label="All"
          @click="rtoggle"
        />
        
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
            @click="rsel"
          > 
            {{ option }}
          </v-chip>
        </v-chip-group>
      </v-card-text>

      <!-- LOCATION GROUP --> 

      <v-card-text>
        <h2 class="title mb-2">
          Locations
        </h2>

        <v-switch
          v-model="active"
          label="All"
          @click="ltoggle"
        />
        
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
            @click="lsel"
          > 
            {{ campus }}
          </v-chip>
        </v-chip-group>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
  import { bus } from '../main'
  export default {
    name:'App',
    data: () => ({
      campuses:['Santa Cruz', 'Los Angeles', 'Merced', 'Riverside', 'Davis', 'San Diego', 'Santa Barbara', 'Berkeley', 'Irvine', 'San Francisco'], 
      options:['Wellness','Food','Housing','Finance','Other'],
      resources:[], 
      locations:[],
      active: false,
      ractive: false,
    }),
    methods: {
      lselected(){
        var value = Object.values(this.locations);
        var selected = []
        value.sort()

        for(var i=0; i<value.length; i++){
          selected.push(this.campuses[value[i]])

        }
        return selected

      },
      rselected(){
        var value = Object.values(this.resources);
        var selected = []
        value.sort()

        for(var i=0; i<value.length; i++){
          selected.push(this.options[value[i]])

        }
        return selected

      },
      ltoggle(){
        if (this.active == false){
          while (this.locations.length != 0){ 
            this.locations.pop()
          }
        } else {
        var i; 
          for (i=0; i < this.campuses.length; i++){
            this.locations.push(i)
          }
        }
        bus.$emit('lsel',this.lselected())
      }, 
      rtoggle(){
        if (this.ractive == false){
          while (this.resources.length != 0){ 
            this.resources.pop()
          }
        } else {
        var i; 
          for (i=0; i < this.options.length; i++){
            this.resources.push(i)
          }
        }
        bus.$emit('rsel',this.rselected())
      }, 
      rsel(){
        if (this.ractive == true){ 
          this.ractive = false
        }
        bus.$emit('rsel',this.rselected())
      },
      lsel(){ 
        if (this.active == true){ 
          this.active = false
        }

        bus.$emit('lsel',this.lselected())
      },

    }
  }

</script>