<template>
  <v-card-text>
    <div class="dashBoard">
      <v-col
        cols="12"
        sm="2"
      >
        <v-sheet
          rounded="lg"
          min-height="268"
          <dashSideBar/>
        >
          <!--  -->
        </v-sheet>
      </v-col>

    </div>
  </v-card-text>
</template>

<script>
  import dashSideBar from '../components/dashSideBar.vue'
  export default {
  components: {dashSideBar}
  }

</script>
