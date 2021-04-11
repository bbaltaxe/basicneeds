<template>
  <v-alert
    dense
    outlined
    type="error"
    color="red"
  >
    {{ msg }}
  </v-alert>
</template>

<script>
export default {
    props: ["msg"],
}


</script>