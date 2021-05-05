<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card
          class="d-flex mb-6"
          height="100"
          @click="remove && adminSelect()"
        >
          <v-card
            v-for="(value,name) in info"
            :key="name"
            class="pa-2"
            flat
          >
            <b>
              {{ name }}:
            </b>
            <br>
            <div v-if="directPrint(value)">
            {{ value }}
            </div>
            <div 
            v-else 
            v-for="item in value"
            :key="item"
            > 
            {{item}}
            </div>
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
    }),
    created (){
      bus.$on('enableEditResource', (data) => {
        this.remove = data;
      })
    }, 
    methods: {
      adminSelect(){
          this.$nextTick(() => {
            bus.$emit('editResource',this.info)
          })

      },
      directPrint(x){
        if (typeof x == 'string' || typeof x == 'boolean') return true
        else return false
      },
    },
  };

</script>