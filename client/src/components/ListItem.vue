<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        {{selected}}
        <v-card
          class="d-flex mb-6"
          height="100"
          @click="remove && adminSelect()"
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
            <v-overlay
              :absolute="absolute"
              :value="remove"
              :opacity=".2"
            >
            </v-overlay>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
  import { bus } from '../main'
  export default {
    name: "ListItem",
    props: {
      info: Object, 
      default: [],
    },
    data: () => ({
      remove: false,
      absolute: true,
      selected: false,
    }),
    created (){
      bus.$on('remove', (data) => {
        this.remove = data;
      })
    }, 
    methods: {
      adminSelect(){
        if (this.selected == false){
          this.selected = true
          this.$nextTick(() => {
            bus.$emit('editResource',this.info)
          })
          
        } else {
          this.selected = false
        }
      }
    },
  };

</script>