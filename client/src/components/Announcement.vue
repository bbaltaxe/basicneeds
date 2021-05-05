<template>
  <v-container>
    <v-card
    @click="remove && adminSelect()"
    >
    <v-row>
      <v-col cols="6">
     <v-card-title>
        <span class="headline">{{info.Title}}</span>
      </v-card-title>
      <v-card-text>
        {{info.Description}}

      </v-card-text>
    </v-col>
    <v-col cols="6">
      <v-card>
      <v-img
          :src="info.Image"
          contain
        ></v-img>
      </v-card>
</v-col>
</v-row>
      <v-overlay
              :absolute="absolute"
              :value="remove"
              :opacity=".2"
            >
            </v-overlay>
    </v-card>

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
      bus.$on('enableEditAnnouncement', (data) => {
        this.remove = data;
      })
    }, 
    methods: {
      adminSelect(){
          this.$nextTick(() => {
            bus.$emit('editAnnouncement',this.info)
          })

      },
      directPrint(x){
        if (typeof x == 'string' || typeof x == 'boolean') return true
        else return false
      },
    },
  };

</script>