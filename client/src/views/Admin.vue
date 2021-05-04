<template>
  <v-container>
    <alert v-if="showError" :msg="alertMessage" />
    <v-container>
      <v-row>
        <v-text-field v-model="name" label="name" required />
        <v-col cols="auto" md="4"> </v-col>
        <v-text-field v-model="email" label="email" required />
      </v-row>
    </v-container>
    <v-select
      v-model="campusSelection"
      :items="campuses"
      item-text="campus"
      item-value="campus"
      label="Campus"
      dense
      outlined
      return-object
    >
    </v-select>

    <v-select
      v-model="resourceSelection"
      :items="resourceTypes"
      item-text="resourceType"
      item-value="resourceType"
      label="Resource"
      dense
      outlined
      return-object
    >
    </v-select>
    <v-container class="px-0" fluid>
       <v-chip-group
              column
              multiple
              v-model="dayOptions"
            >
              <v-chip
                v-for="day in days"
                :key="day"
                filter 
                outlined
              > 
                {{ day }}
              </v-chip>
            </v-chip-group>
    </v-container>
    <v-text-field v-model="hours" label="hours" required />
    <v-text-field v-model="description" label="description" required />
    <v-btn color="success" class="mr-4" @click="onSubmit">
      Register Service
    </v-btn>
  </v-container>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";

export default {
  components: {
    alert: Alert,
  },
  data() {
    return {
      name: "",
      email: "",
      days: [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ],
      dayOptions: "",
      campuses: [
        { campus: "UCR" },
        { campus: "UCB" },
        { campus: "UCM" },
        { campus: "UCSB" },
        { campus: "UCI" },
        { campus: "UCSD" },
        { campus: "UCSC" },
        { campus: "UCLA" },
        { campus: "UCD" },
        { campus: "UCSF" },
      ],
      campusSelection: "",
      resourceTypes: [
        { resourceType: "Food" },
        { resourceType: "Wellness" },
        { resourceType: "Housing" },
        { resourceType: "Finance" },
        { resourceType: "Other" },
      ],
      resourceSelection: "",

      description: "",
      hours: "",
      showError: false,
      apiRoot: process.env.VUE_APP_API_ROOT,
    };
  },
  methods: {
    initForm() {
      this.name = "";
      this.description = "";
      this.hours = "";
      this.email = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      const path = `http://${this.apiRoot}/admin/addservice`;
      const payload = {
        name: this.name,
        campus: this.campusSelection["campus"],
        resource_type: this.resourceSelection["resourceType"],
        description: this.description,
        hours: this.hours,
        email: this.email,
      };
      console.log(payload);
      axios
        .post(path, payload)
        .then((response) => {
          console.log(response);
          if (response.data["status"] === "success") {
            this.$router.push("/add");
          } else {
            this.alertMessage = response.data["msg"];
            this.showError = true;
            this.initForm();
          }
        })
        .catch((error) => {
          console.log(error);
        });
      this.initForm();
    },
  },
};
</script>