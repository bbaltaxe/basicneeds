<template>
  <div id="app">
    <v-app id="inspire">
      <v-card
        class="mx-auto"
        max-width="500"
      >
        <v-list >
          <v-list-item-group v-model="model" >
            <v-list-item
              v-for="(item, i) in items"
              :key="i"
              :to="item.endpoint"
            >
              <v-list-item-icon >
                <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon >

              <v-list-item-content >
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list> 
      </v-card>
    </v-app>
  </div>
</template>

<script>
  export default {
    data: () => ({
      items: [
        {
          icon: 'mdi-square',
          text: 'My DashBoard',
          endpoint:'/dashBoard',
        },
        {
          icon: 'mdi-star',
          text: 'My Resources',
          endpoint:'/myResources'
        },
        {
          icon: 'mdi-plus',
          text: 'Add Resources',
          endpoint:'/add'
        },

      ],
      model: 1,
    }),
  }
</script>
