<template> 
      
<v-container>
    <alert v-if="showError" :msg=alertMessage></alert>
   <v-text-field
      v-model="name"
      label="name"
      required
    ></v-text-field>
<v-text-field
      v-model="password"
      label="password"
      required
    ></v-text-field>

    <v-btn
      color="success"
      class="mr-4"
      @click="onSubmit"
    >
      Login
    </v-btn>

</v-container>


</template> 

<script>
import axios from 'axios';
import Alert from '../components/Alert.vue';
export default {

    data() {
        return {
            name: "",
            password:"",
            response:"",
            alertMessage: "",
            showError: false,
            apiRoot: process.env.VUE_APP_API_ROOT,
        }
    },
    components:{
        alert: Alert,
    },
    methods: {
            initForm(){
                this.name = "";
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
                const path = `http://${this.apiRoot}:5000/duo`;
                const payload = {
                    name: this.name,
                    password: this.password,
                };
                this.validate();
                axios.post(path, payload)
                    .then((response)=> {
                        console.log(response);
                        if(response.data['is_redirect'] === "true"){
                            console.log(response.data['redirect_url']);
                        }else{
                                this.showError = true;
                                console.log(response.data['msg']);
                                this.alertMessage = response.data["msg"];
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


