<template>
	<v-card-text>
		<div class="home">
			<h1>welcome home!</h1>
			<v-btn to="/campus"
				elevation="2"
				plain
				Login
				x-large
			></v-btn>

		</div>


  <v-container fluid>
    <v-row>
      <v-col cols="10">
        <v-combobox
          v-model="select"
          :items="items"
          label="Resources"
          multiple
          outlined
          dense
        ></v-combobox>
      </v-col>
    </v-row>
  </v-container>
	</v-card-text>
</template>

<script>
  export default {
    data () {
      return {
        select: [],
        items: [
          'Food ',
          'Mental Wellbeing',
          'Housing',
          'Financial',
        ],
      }
    },
  }
</script>
