<template>
  <div>
    <ListItem
      v-if="matchingItems(selectedCampuses,thisinfo.Campus) && matchingItems(selectedResources, thisinfo.Resource)"
      :info="thisinfo"
    />
    <ListItem
      v-if="matchingItems(selectedCampuses,otherinfo.Campus) && matchingItems(selectedResources, otherinfo.Resource)"
      :info="otherinfo"
    />

  </div>
</template>


<script>
  import { bus } from '../main'
  import ListItem from '../components/ListItem.vue'
  export default {
    components: {ListItem}, 
	data: () => ({
  
		selectedCampuses: [],
		selectedResources: [],
    // this is probably where we need to suck things in from the database 
    thisinfo: {
        Campus: ['Santa Cruz'], 
        Location: "Address / Building",
        Resource: ['Food'],
        Name: "SUA Food Pantry & Lounge", 
        Description: "Choice-based food pantry and lounge space. Fresh produce, ready-to-eat meals, and non-perishable. Snacks, coffee, tea, & microwave are available", 
        Hours: "Mon-Sat 10am-4pm", 
        Contact: "bre@ucsc.edu",
        Added: false,
      },
    otherinfo: {
        Campus: ['San Diego','Merced'], 
        Location: "Address / Building",
        Resource: ['Housing'],
        Name: "Housing Resource", 
        Description: "Description", 
        Hours: "Mon-Sat 10am-4pm", 
        Contact: "bbaltaxe@ucsc.edu",
        Added: false,
      },
  	}),
    methods: {
        matchingItems(ar1, ar2){
          for(var i in ar1){
            if (ar2.includes(ar1[i])){
              return true
            } 
          }
          return false
        }
    },
  	created (){
	    bus.$on('lsel', (data) => {
	      this.selectedCampuses = data;
	    })
	    bus.$on('rsel', (data) => {
	      this.selectedResources = data;
	    })
  	}
  }
</script>