<template> 
	<div class="about">
		<v-card-text>
			<h1>About</h1>
			<p>An ecosystem that supports financial stability by ensuring equitable access to nutritious and sufficient food; safe, secure, and adequate housing (to sleep, study, cook, and shower); healthcare to promote sustained mental and physical well-being; affordable transportation; resources for personal hygiene care; and emergency needs for students with dependents.</p>

			Here's a list of campuses to show server communication: 
			<li v-for="campus in campuses" :key=campus>{{campus}}</li>
		</v-card-text>

		
	</div>
</template> 

<script>
	//talk to the server
	import axios from 'axios';
	export default {
		data () {
		return {
			loading: true, 
			apiRoot: process.env.VUE_APP_API_ROOT, 
			campuses: null
		}
	},
	mounted () {
	axios
		.get(`http://${this.apiRoot}:5000/campuses`)
		.then(response => {
			this.wholeResponse = response.data.Search;
			this.loading = false;
			this.campuses = response.data.campuses; 
		})
		.catch(error => {
			console.log(error)
		})
	}	
	}
</script>