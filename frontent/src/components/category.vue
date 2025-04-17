<script>
import axios from "axios";

export default {
  data() {
    return {
      R_C_name: "",
      error: "",
      requestcategory: [],
    };
  },
  methods: {
    postcategory() {
      if (this.R_C_name != "") {
        const token = sessionStorage.getItem("user");
        if (token) {
          console.log(token);
          axios({
            url: "http://127.0.0.1:5000//categoryProduct",
            method: "POST",
            data: {
              R_C_name: this.R_C_name,
              R_C_type: "POST",
            },

            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
            // 20/05/2024
          })
            .then((response) => {
              alert(response.data.message);
              this.getcategory();

              console.log(" After Api Success prduct");
              (this.R_C_name = ""),
                (this.error = ""),
                (this.R_C_type = ""),
                (this.R_approved = "");
            })
            .catch((error) => {
              console.log(error);
            });
        } else {
          alert("Please Login");
        }
      } else {
        this.error = "Please fill out the category name!";
      }
    },

    async getcategory() {
      const token = sessionStorage.getItem("user");
      try {
        const response = await axios.get(
          "http://127.0.0.1:5000/categoryProduct",
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`, // Include the token in the Authorization header
            },
          }
        );
        this.requestcategory = response.data;
        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    },
    deletereq(req) {
      const token = sessionStorage.getItem("user");

      axios({
        url: "http://127.0.0.1:5000/categoryProduct",
        method: "DELETE",
        data: {
          R_id: req.R_id,
        },

        headers: {
          "Content-Type": "application/json",
          "Authorization ": `Bearer ${token}`,
        },
      })
        .then((response) => {
          alert("response.data");
          console.log("Success");
          this.getcategory();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getcategory();
  },
};
</script>
<template>
  <div class="product">
    <div class="listprodsreq">
      <p>{{ requestcategory }}</p>
      <div v-for="req in requestcategory" :key="req">
        <p>{{ req.R_C_name }}</p>

        <p>{{ req.R_C_type }}</p>
        <button v-on:click="deletereq(req)">Delete</button>
      </div>
    </div>
    <div class="box">
      <div class="form">
        <h1>Add Category</h1>
        <div class="input_form">
          <label class="label">Category Name</label>
          <input class="field_input" type="text" v-model="R_C_name" placeholder="Category Name" />
          <div class="error">{{ error }}</div>
          <button class="login-btn" v-on:click="postcategory">Add</button>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.product {
  display: flex;
}

h1 {
  text-align: center;
  margin-bottom: 35px;
}

.box {
  display: flex;
  align-content: center;
  justify-content: center;
  width: 100%;
}

.form {
  width: 50%;
  padding: 20px;
  margin: 20px 0px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

@media (max-width: 500px) {
  .form {
    width: 100%;
    margin: 10px;
  }
}

/* .input_form {
  width: 95%; *
  box-sizing: border-box;
} */
.field_input {
  width: 100%;
  padding: 5px 10px;
  /* height: 30px; */
  /* margin-bottom: 10px; */
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

.label {
  margin: 7px 6px;
  font-weight: 500;
  font-size: 16px;
}

.cloudinary-button {
  border: none;
  outline: none;
  padding: 6px 14px;
  border-radius: 5px;
  background: seagreen;
  color: white;
}

.cloudinary-button:hover {
  background-color: rgb(58, 160, 102);
}

.login-btn {
  width: 100%;
  margin-top: 50px;
  height: 40px;
  background-color: seagreen;
  border-radius: 5px;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 18px;
  transition-duration: 0.3s;
}

.login-btn:hover {
  background-color: rgb(58, 160, 102);
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}
</style>
