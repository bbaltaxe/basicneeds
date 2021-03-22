<template> 

      
<v-container>
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
export default {

    data() {
        return {
            name: "",
            password:"",
            response:"",
        }
    },
    methods: {
            
            onSubmit(evt){
                evt.preventDefault();
                const path = 'http://localhost:5000/duo';
                const payload = {
                    name: this.name,
                    password: this.password,
                };
                axios.post(path, payload)
                    .then((res)=> {
                        console.log(res);
                        window.location.href = res;

                })
                     .catch((error)=> {
                         console.log(error);
                });
            }
    }
}


</script>


