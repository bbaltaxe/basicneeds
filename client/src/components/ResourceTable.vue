<template>
  <div>
    <table>
      <thead>
        <tr>
          <th scope="col">
            Campus
          </th>
          <th scope="col">
            Resource
          </th>
          <th scope="col">
            Type
          </th>
          <th scope="col">
            Date(s)
          </th>
        </tr>
      </thead>
      <tbody>
        <td>ucsc</td>
        <td>food pantry</td>
        <td>food</td>
        <td>April 1 2020</td>
        <td>
          <v-btn
            elevation="14" 
          >
            Add
          </v-btn>
        </td>
      </tbody>
    </table>
    <ListItem />
  </div>
</template>

          <script>
            
  import ListItem from '../components/ListItem.vue'
  export default {
    components: {ListItem}
  }
          </script>