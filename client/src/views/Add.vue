<template> 
  <v-card-text>
    <div class="add">
      <h1>Add Resources to your Home Page</h1>

  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-toolbar
      flat
      color="deep-purple accent-4"
      dark
    >
      <v-btn icon>
        <v-icon>mdi-close</v-icon>
      </v-btn>
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

      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-select
          :items="sortby"
          label="Sort By"
          solo
        ></v-select>
      </v-col>
    </div>
  </v-card-text>
</template> 

<script>
  export default {
    data: () => ({
      sortby: ['Date', 'Location', 'Resource Type', 'Popularity', 'Random'],
      location: ['here']
    }),
  }
</script>

