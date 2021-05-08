<template>
  <div>
    <Announcement
      :info="thisinfo"
    />
    <br>
    <Announcement
      :info="otherinfo"
    />
    <br>
    <!-- Sorting code, but don't sort for now: 

    <Announcement
      v-if="matchingItems(selectedCampuses,thisinfo.Campus) && matchingItems(selectedResources, thisinfo.Resource)"
      :info="thisinfo"
    />
    <br>
    <Announcement
      v-if="matchingItems(selectedCampuses,otherinfo.Campus) && matchingItems(selectedResources, otherinfo.Resource)"
      :info="otherinfo"
    />
    <br>
  -->
  </div>
</template>


<script>
  import { bus } from '../main'
  import Announcement from '../components/Announcement.vue'
  export default {
    components: {Announcement}, 
	data: () => ({
  
		selectedCampuses: [],
		selectedResources: [],
    // this is probably where we need to suck things in from the database 
    thisinfo: {
        Title: 'Welcome', 
        Description: "Welcome to our new web portal for basic needs access!",
        Image: 'https://images.unsplash.com/photo-1550850395-c17a8e90ad0a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=3334&q=80',
        AltText: 'colorful helium balloons float in a blue sky with one white cloud',
        PostDate: '2021-05-05', 
        RemoveDate: '2021-06-06',
        Campus: ['San Diego','Merced','Santa Cruz'],
        Resource: ['Food'],
      },
    otherinfo: {
        Title: 'Welcome also to cats', 
        Description: "Welcome to our new web portal for basic needs access!",
        Image: 'https://static01.nyt.com/images/2020/04/22/science/22VIRUS-PETCATS1/merlin_150476541_233fface-f503-41af-9eae-d90a95eb6051-superJumbo.jpg?quality=90&auto=webp',
        AltText: 'colorful helium balloons float in a blue sky with one white cloud',
        PostDate: '2021-05-05', 
        RemoveDate: '2021-06-06',
        Campus: ['Riverside'],
        Resource: ['Housing'],
      },
  	}),
  	created (){
	    bus.$on('lsel', (data) => {
	      this.selectedCampuses = data;
	    })
	    bus.$on('rsel', (data) => {
	      this.selectedResources = data;
	    })
  	},
    methods: {
        matchingItems(ar1, ar2){
          for(var i in ar1){
            if (ar2.includes(ar1[i])){
              return true
            } 
          }
          return false
        }
    }
  }
</script>