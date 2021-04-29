<template>
  <div>
    <ListItem
      v-if="selectedCampuses.includes(thisinfo.Location) && selectedResources.includes(thisinfo.Resource)"
      :info="thisinfo"
    />
    <ListItem
      v-if="selectedCampuses.includes(otherinfo.Location) && selectedResources.includes(otherinfo.Resource)"
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
        Location: 'Santa Cruz', 
        Resource: 'Food',
        Name: "SUA Food Pantry & Lounge", 
        Description: "Choice-based food pantry and lounge space. Fresh produce, ready-to-eat meals, and non-perishable. Snacks, coffee, tea, & microwave are available", 
        Hours: "Mon-Sat 10am-4pm", 
        Added: false,
      },
    otherinfo: {
        Location: 'San Diego', 
        Resource: 'Housing',
        Name: "Housing Resource", 
        Description: "Description", 
        Hours: "Mon-Sat 10am-4pm", 
        Added: false,
      },
  	}),
    methods: {
        
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