<script>
import axios from 'axios';
// import Vuecookies from 'vue-cookies';




export default {

    data() {
        return {
            Email_id: '',
            Username: '',
            message: '',
            token: '',
            emailid: '', // Adding emailid to hold the user input
            password: '' // Adding password to hold the user input

        }
    },

    methods: {
        async Login() {
            try {
                axios({
                    method: 'POST',
                    url: 'http://127.0.0.1:5000/userlogin',
                    data: {

                        emailid: this.emailid,
                        Password: this.password

                    }
                }).then(response => {
                    this.Email_id = response.data.Email_id || '';
                    this.Username = response.data.Username || '';
                    this.message = response.data.message || '';
                    this.token = response.data.token || '';

                    (async () => {
                        const module = await import('jwt-decode');
                        let jwtDecode = module.jwtDecode || module;
                        let detail = jwtDecode(response.data.token);
                        if (detail.sub.Role == 'ADMIN') {
                            alert("ADMIN Wellcome")
                            this.$cookies.set('token', response.data.token, '1d');
                            this.$router.push({ name: 'adminmain' });
                        }else{
                            alert("You are NOt ADMIN")
                        }
                    })();

                })

            } catch (error) {
                console.error('Invalid JWT token', error);
            }

        },

    },
    mounted() {
        console.log(`This is a count. ${this.emailid} and ${this.password}`)
    }
}
</script>

<template>
    <div class="admin" >
        <form class="form">
            <h1>Admin</h1>
            <input v-model="emailid" placeholder="Email ID" />
            <input v-model="password" placeholder="password" />

            <button @click="Login()">Login</button>
        </form>
        
    </div>
</template>
<style>
.form{
    
    background-color: black;
    width: 500px;
    height: 400px;
    margin-left: 100%;
    margin-top: 100px;

}
.admin{
    background-image: url("D:\Faizan\Resume_project\frountend\Grocery Store\src\assets\src\istockphoto-1449032425-1024x1024.jpg");
    height: 600px;
    width: 800px;
}

</style>