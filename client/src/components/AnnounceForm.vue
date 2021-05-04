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
          <span class="headline">New Announcement</span>
        </v-card-title>



        <v-card-text>
          <v-text-field
            label="Title*"
            v-model="title"
            required
          />

          <v-textarea
            label="Description*"
            v-model="description"
            counter
            maxlength="120"
            full-width
            single-line
            required
          />

          <v-row>
            <v-col
              cols="12"
              lg="6"
            >
              <v-text-field
                v-model="urlLink"
                label="Url to image"
              />
            </v-col>
            <v-col
              cols="12"
              lg="6"
            >
              <v-text-field
                v-model="altText"
                label="Alt text for image"
              />
            </v-col>
          </v-row>


          <v-row>
            <v-col
              cols="12"
              lg="6"
            >
              <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                :return-value.sync="date"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="date"
                    label="Post Date*"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  />
                </template>
                <v-date-picker
                  v-model="date"
                  no-title
                  scrollable
                >
                  <v-spacer />
                  <v-btn
                    text
                    color="primary"
                    @click="menu = false"
                  >
                    Cancel
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.menu.save(date)"
                  >
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>

            <v-col
              cols="12"
              lg="6"
            >
              <v-menu
                ref="menu2"
                v-model="menu2"
                :close-on-content-click="false"
                :return-value.sync="date2"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="date2"
                    label="Remove Date*"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  />
                </template>
                <v-date-picker
                  v-model="date2"
                  no-title
                  scrollable
                >
                  <v-spacer />
                  <v-btn
                    text
                    color="primary"
                    @click="menu2 = false"
                  >
                    Cancel
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.menu2.save(date2)"
                  >
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>
          </v-row>

          <v-card-text>
            Relevant Resources*

            <v-chip-group
              column
              multiple
              v-model="serviceOptions"
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
              column
              multiple
              v-model="locations"
            >
              <v-chip
                v-for="campus in campuses"
                :key="campus"
                filter 
                outlined
              > 
                {{ campus }}
              </v-chip>
            </v-chip-group>
          </v-card-text>
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
            @click="dialog = false & passForm()"
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
      date: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      dialog: false,
      menu: false,
      menu2: false,
      campuses:['Santa Cruz', 'Los Angeles', 'Merced', 'Riverside', 'Davis', 'San Diego', 'Santa Barbara', 'Berkeley', 'Irvine', 'San Francisco'], 
      locations:[],
      options:['Wellness','Food','Housing','Finance','Other'],
      serviceOptions: [],
      title: "",
      description:"",
      urlLink:"",
      altText:"",
    }),
    methods: {
      passForm(){
        var payload = {
          title: this.title,
          description: this.description,
          urlLink: this.urlLink,
          altText: this.altText,
          campus: this.lselected(),
          option: this.rselected(),
          postDate: this.date,
          removeDate: this.date2,
        }
        this.$emit("submitAnnouncement", payload)
        
      },
       lselected(){
        var value = Object.values(this.locations);
        var selected = []
        value.sort()

        for(var i=0; i<value.length; i++){
          selected.push(this.campuses[value[i]])

        }

        return selected

      },
      rselected(){
        var value = Object.values(this.serviceOptions);
        var selected = []
        value.sort()

        for(var i=0; i<value.length; i++){
          selected.push(this.options[value[i]])

        }
        return selected

      },
    },
    emits: [
      "submitAnnouncement",
    ],
    
  }
</script>