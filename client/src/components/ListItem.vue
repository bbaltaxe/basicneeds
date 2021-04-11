<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card
          class="d-flex mb-6"
          height="100"
        >
          <v-card
            v-for="(value,name) in info"
            :key="value"
            class="pa-2"
          >
            {{name}}:
            <br>
            {{value}}
          </v-card>
          
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "HelloWorld",
  data: () => ({
    // this is probably where we need to suck things in from the database 
    info: {
        Location: 'UCSC', 
        Resource: 'Food',
        Name: "SUA Food Pantry & Lounge", 
        Description: "Choice-based food pantry and lounge space. Fresh produce, ready-to-eat meals, and non-perishable. Snacks, coffee, tea, & microwave are available", 
        Hours: "Mon-Sat 10am-4pm", 
        Added: false,
      },
  }),
};
</script>