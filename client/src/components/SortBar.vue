<template> 
  <v-col
    class="d-flex"
    cols="12"
    sm="6"
  >
    <v-select
      :items="sortby"
      label="Sort By"
      solo
    />
  </v-col>
</template>

<script>
  export default {
    data: () => ({
      sortby: ['Date', 'Location', 'Resource Type', 'Popularity', 'Random'],
    }),
  }
</script>
