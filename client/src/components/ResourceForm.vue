<template>
  <div>
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="green"
          dark
          elevation="0"
          v-bind="attrs"
          v-on="on"
        >
          Add
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Add Resource</span>
        </v-card-title>


        <v-card-text>
          <v-text-field
            label="Title*"
            required
            v-model="name"
          />

          <v-textarea
            label="Description*"
            counter
            maxlength="120"
            full-width
            single-line
            required
          />

          <v-text-field 
            v-model="hours" 
            label="Hours" 
            hint="Ex: MWF 3pm-5pm, TTh 11am-2pm"
            required 
          />

          <v-card-text>
            Relevant Resources*

            <v-chip-group
              column
              multiple
            >
              <v-chip
                v-for="option in options"
                :key="option"
                filter 
                outlined
              > 
                {{ option }}
              </v-chip>
            </v-chip-group>
          </v-card-text>

          <v-card-text>
            Relevant Campuses*
            <v-chip-group
              v-model="locations" 
              column
              multiple
            >
              <v-chip
                v-for="campus in campuses"
                :key="campus"
                filter 
                outlined
                @click="lsel"
              > 
                {{ campus }}
              </v-chip>
            </v-chip-group>
          </v-card-text>

          <v-text-field v-model="email" label="Contact Email" />

        </v-card-text>

        


        <v-card-actions>
          <v-spacer />
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Cancel
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
  export default {
    data: () => ({
      dialog: false,
      name: "",
      description: "",
      hours: "",
      email: "",
      campuses:['Santa Cruz', 'Los Angeles', 'Merced', 'Riverside', 'Davis', 'San Diego', 'Santa Barbara', 'Berkeley', 'Irvine', 'San Francisco'], 
      options:['Wellness','Food','Housing','Finance','Other'],
    }),
    methods: {
      initForm() {
        this.name = "";
        this.description = "";
        this.hours = "";
        this.email = "";
      },
    }, 
  }
</script>