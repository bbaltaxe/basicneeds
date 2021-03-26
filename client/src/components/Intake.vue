<template>
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
