import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Groceries from './views/Groceries.vue'
import Housing from './views/Housing.vue'
import MentalWellbeing from './views/MentalWellbeing.vue'
import Campus from './views/Campus.vue'
import Intake from './components/Intake.vue'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
import Login from './components/Login.vue'
import HomePage from './components/HomePage.vue'
import Popup from './components/Popup.vue'

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
			path: '/campus',
			name: 'Choose Campus',
			component: Campus
		},
		{
			path: '/intake',
			name: 'intake form',
			component: Intake
		},
		{
			path: '/hello',
			name: 'hello world',
			component: HelloWorld
		},
		{
			path: '/navBar',
			name: 'nav bar',
			component: NavBar
		}
		,
		{
			path: '/homepage',
			name: 'home page',
			component: HomePage
		},
		{
			path: '/Popup',
			name: 'Popup',
			component: Popup
		}

	]

})
