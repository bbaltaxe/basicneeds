<template>
  <div>
    <v-card
      class="mr-auto"
      max-width="300"
    >
      <v-toolbar
        flat
        color="grey accent-4"
        dark
      >
        <v-toolbar-title>Filter Results</v-toolbar-title>
      </v-toolbar>

      <v-card-text>
        <h2 class="title mb-2">
          Resource Type
        </h2>

        <v-chip-group
          v-model="resources"
          column
          multiple
        >
          <v-chip
            filter
            outlined
          >
            Wellness
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Food
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Housing
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Finance
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Other
          </v-chip>
        </v-chip-group>
      </v-card-text>

      <v-card-text>
        <h2 class="title mb-2">
          Locations
        </h2>

        <v-chip-group
          v-model="location"
          column
          multiple
        >
          <v-chip
            filter
            outlined
          >
            Santa Cruz
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Los Angeles
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Merced
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Riverside
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Davis
          </v-chip>
          <v-chip
            filter
            outlined
          >
            San Diego
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Santa Barbara
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Berkeley
          </v-chip>
          <v-chip
            filter
            outlined
          >
            Irvine
          </v-chip>
          <v-chip
            filter
            outlined
          >
            San Francisco
          </v-chip>
        </v-chip-group>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
  export default {
    name:'App',
    data () {
      return {}
    }
  }

</script>