<template>
  <v-container>
    <v-card-text>
      <h1>Register</h1>
    </v-card-text>

    <alert 
      v-if="showError" 
      :msg="alertMessage"
    />
    <v-text-field
      v-model="username"
      label="name"
      required
    />
    <v-text-field
      v-model="password"
      label="password"
      required
    />

    <v-btn
      color="success"
      class="mr-4"
      @click="onSubmit"
    >
      Register
    </v-btn>
  </v-container>
</template>

<script>
import axios from 'axios';
import Alert from '../components/Alert.vue';

export default {
    components:{
        alert: Alert,
    },
    data() {
        return {
            username: "",
            password:"",
            response:"",
            alertMessage: "",
            showError: false,
            apiRoot: process.env.VUE_APP_API_ROOT,
        }
    },
    methods: {
            initForm(){
                this.username = "";
                this.password = "";
            }, 
            validate(){
                if(this.name === "" || this.password === ""){
                    this.showError = true;
                    this.alertMessage = "Please enter username and/or password";
                    this.initForm();
                } 
            },
            onSubmit(evt){
                evt.preventDefault();
                const path = `http://${this.apiRoot}/auth/register`;
                const payload = {
                    username: this.username,
                    password: this.password,
                };
                this.validate();
                console.log(payload)
                axios.post(path, payload)
                    .then((response)=> {
                      console.log(response)
                      if(response.data['insert_status'] === "success"){
                          this.$router.push('/login');
                      } else{
                        this.alertMessage = response.data['msg'];
                        this.showError = true;
                        this.initForm();
                      }
                    })
                    .catch((error)=> {
                         console.log(error);
                });
                this.initForm();
            }
    }
}
</script>