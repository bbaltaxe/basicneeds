<template> 
      
<v-container>
    <alert :message=alertMessage v-if="showError"></alert>
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
            onSubmit(evt){
                evt.preventDefault();
                const path = 'http://localhost:5000/duo';
                const payload = {
                    name: this.name,
                    password: this.password,
                };
                axios.post(path, payload)
                    .then((response)=> {
                        console.log(response);
                        if(response.data['is_redirect'] === "true"){
                            //window.location.href = response.data['redirect_url'];
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


