import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Groceries from './views/Groceries.vue'
import Housing from './views/Housing.vue'
import MentalWellbeing from './views/MentalWellbeing.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'

Vue.use(Router)

export default new Router({

	mode: 'history',
	base: process.env.BASE_URL, 
	routes:[
		{
			path: '/',
			name: 'home',
			component: Home
		},
		{
			path: '/about',
			name: 'about',
			component: About
		},
		{
			path: '/groceries',
			name: 'groceries',
			component: Groceries
		},
		{
			path: '/housing',
			name: 'housing',
			component: Housing
		},
		{
			path: '/mental_wellbeing',
			name: 'mental_wellbeing',
			component: MentalWellbeing
		},
		{
			path: '/login', 
			name: 'login',
			component: Login
		},
		{
			path: '/register',
			name: 'register',
			component: Register
		}

	]

})