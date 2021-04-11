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
          v-on:click="rtoggle"
        />
        
        <v-chip-group
          column 
          multiple
          v-model="resources"
        >
          <v-chip
            v-for="option in options"
            :key="option"
            filter 
            outlined
            v-on:click="rsel"
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
          v-on:click="ltoggle"
        />
        
        <v-chip-group
          column 
          multiple
          v-model="locations"
        >
          <v-chip
            v-for="campus in campuses"
            :key="campus"
            filter 
            outlined
            v-on:click="lsel"
          > 
            {{ campus }}
          </v-chip>
        </v-chip-group>
      </v-card-text>
    </v-card>


    <span>resources: {{ resources }}</span>
    <span>locations: {{ locations }}</span>
  </v-container>
</template>

<script>
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
      }, 
      rsel(){
        if (this.ractive == true){ 
          this.ractive = false
        }
      },
      lsel(){
        if (this.active == true){ 
          this.active = false
        }
      },
    }
  }

</script>