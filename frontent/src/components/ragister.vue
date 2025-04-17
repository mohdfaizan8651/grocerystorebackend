<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      Email_id: "",
      Username: "",
      message: "",
      type: "manager",
      token: "",
      emailid: "", // Adding emailid to hold the user input
      password: "", // Adding password to hold the user input
      error: "",
    };
  },

  methods: {
    ragister() {
      if (this.emailid && this.Username && this.password) {
        axios({
          method: "POST",
          url: "http://127.0.0.1:5000/userragister",
          data: {
            emailid: this.emailid,
            Username: this.Username,
            Password: this.password,
            Role: this.type,
          },
        }).then((response) => {
          console.log(response.data.Roll);
          if (response.data.message == "Ragister successfully") {
            this.$router.push("/Login");
            this.Email_id = response.data.Email_id || "";
            this.Username = response.data.Username || "";
            this.message = response.data.message || "";
            this.token = response.data.token || "";
          } else {
            alert("Something went wrong", response.data.message);
          }
        });
      } else {
        this.error = "*Please fill out all fields";
      }
    },
  },
  mounted() {
    console.log(`This is a count. ${this.emailid} and ${this.password}`);
  },
};
</script>

<template>
  <div class="login_form">
    <div class="input_form">
      <label class="label">Email</label>
      <input
        v-model="emailid"
        placeholder="Email ID"
        class="field_input" /><br />
      <label class="label">Username</label>
      <input
        v-model="Username"
        placeholder=" Username"
        class="field_input" /><br />
      <label class="label">Password</label>
      <input v-model="password" placeholder="password" class="field_input" />
    </div>
    <div class="radio">
      <input type="radio" id="manager" v-model="type" value="manager" checked />
      <label for="manager">Maneger</label>

      <input type="radio" id="user" v-model="type" value="user" />
      <label for="user">User</label>
    </div>
    <div class="error">{{ error }}</div>

    <button class="login" @click="ragister()">Ragister</button>
  </div>
</template>
<style>
.label {
  margin: 7px 6px;
  font-weight: 500;
  font-size: 16px;
}
h1 {
  text-align: center;
  margin-bottom: 35px;
}
.box {
  display: flex;
  align-content: center;
  justify-content: center;
  margin-top: 100px;
}
.login_form {
  width: 400px;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
.input_form {
  width: 95%;
  box-sizing: border-box;
}
@media (max-width: 500px) {
  .box .login_form {
    width: 100%;
    margin: 10px;
  }
}
.field_input {
  width: 100%;
  padding: 5px 10px;
  /* height: 30px; */
  margin-bottom: 10px;
  border: 1px solid lightgray;
  border-radius: 5px;
  outline: none;
  transition: 0.3s;
}
.field_input:hover {
  border: 1px solid seagreen;
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}
.field_input:focus {
  border: 1px solid seagreen;
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}
.radio {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
/* .radio input[] {
  display: flex;
  justify-content: center;
  margin-top: 20px;
} */
.login-btn {
  width: 100%;
  margin-top: 50px;
  height: 40px;
  font-weight: 500;
  background-color: seagreen;
  border-radius: 5px;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 18px;
  transition: 0.3s;
}
.login-btn:hover {
  background-color: rgb(58, 160, 102);
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}
</style>
