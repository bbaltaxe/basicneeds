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
            <b>
              {{ name }}:
            </b>
            <br>
            {{ value }}
          </v-card>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "ListItem",
  props: {
    info: Object, 
    default: [],
  },
};
</script>