<script>
import axios from "axios";

export default {
  data() {
    return {
      R_id: "",
      R_C_id: "",
      R_P_id: "",
      R_P_name: "",
      R_Unit: "",
      R_Qut: "",
      R_price: "",
      R_MFG: "",
      R_Exp: "",
      R_image: "",
      R_approved: "",
      datetime: "",
      R_user_id: "",
      R_P_type: "",
      requestproduct: [],
      datacategory: [],
      error: "",
    };
  },
  methods: {
    datacate() {
      const token = sessionStorage.getItem("user");
      axios
        .get('http://127.0.0.1:5000/category/""', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          this.datacategory = response.data;
        })
        .catch((error) => {
          console.error("Error fetching category", error);
        });
    },
    requestProduct() {
      // 20/08/-2024
      if (
        this.R_P_name &&
        this.R_Unit &&
        this.R_Qut &&
        this.R_price &&
        this.R_MFG &&
        this.R_Exp &&
        this.R_C_id
      ) {
        const token = sessionStorage.getItem("user");
        if (token) {
          console.log(token);
          axios({
            url: "http://127.0.0.1:5000/requestProduct",
            method: "POST",
            data: {
              R_C_id: this.R_C_id,
              R_P_id: this.R_P_id,
              R_P_name: this.R_P_name,
              R_Unit: this.R_Unit,
              R_Qut: this.R_Qut,
              R_price: this.R_price,
              R_MFG: this.R_MFG,
              R_Exp: this.R_Exp,
              R_image: this.R_image,
              R_P_type: "POST",
            },

            headers: {
              "Content-Type": "application/json",
              "Authorization ": `Bearer ${token}`,
            },
            // 20/05/2024
          })
            .then((response) => {
              alert(response.data);
              this.getproductreqt();

              console.log(" After Api Success prduct");
              (this.R_C_id = ""),
                (this.R_P_name = ""),
                (this.R_Unit = ""),
                (this.R_Qut = ""),
                (this.R_price = ""),
                (this.R_MFG = ""),
                (this.R_Exp = ""),
                (this.R_image = "");
            })
            .catch((error) => {
              console.log(error);
            });
        } else {
          alert("Please Login");
        }
      } else {
        this.error = "*Please fill out all fields";
      }
    },

    getproductreqt() {
      const token = sessionStorage.getItem("user");

      axios({
        url: "http://127.0.0.1:5000/requestProduct",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Authorization ": `Bearer ${token}`,
        },
      })
        .then((response) => {
          this.requestproduct = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
      console.log("Success prduct");
    },
    deletereq(R_id) {
      const token = sessionStorage.getItem("user");

      axios({
        url: "http://127.0.0.1:5000/requestProduct",
        method: "DELETE",
        data: {
          R_id: R_id,
        },

        headers: {
          "Content-Type": "application/json",
          "Authorization ": `Bearer ${token}`,
        },
      })
        .then((response) => {
          alert("response.data");
          console.log("Success");
          this.getproductreqt();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    upload_widget() {
      var myWidget = cloudinary.createUploadWidget(
        {
          cloudName: "dxqf7cs4h",
          uploadPreset: "grocerystore",
        },
        (error, result) => {
          if (!error && result && result.event === "success") {
            this.R_image = result.info.secure_url;
            console.log("Done! Here is the image info: ", result.info);
          }
        }
      );
      console.log(myWidget);
      myWidget.open();
      console.log("afetr", this.R_image);
    },
  },
  mounted() {
    this.getproductreqt();
    this.datacate();
  },
};
</script>
<template>
  <div class="product">
    <div class="listprodsreq">
      <div v-for="req in requestproduct" :key="req">
        <p>{{ req.R_P_name }}</p>
        <p>{{ req.R_Qut }}</p>
        <p>{{ req.R_Unit }}</p>
        <p>{{ req.R_approved }}</p>
        <p>{{ req.R_MFG }}</p>
        <p>{{ req.R_Exp }}</p>
        <p>{{ req.R_P_type }}</p>
        <div class="prod_img">{{ req.R_image }}</div>
        <p>{{ req.R_price }}</p>
        <button
          v-on:click="
            deletereq(
              req.R_id,
              req.R_C_id,
              req.R_P_name,
              req.R_MFG,
              req.R_Exp,
              req.R_Qut,
              req.R_Unit,
              req.R_approved,
              req.R_image,
              req.R_price
            )
          ">
          Delete
        </button>
      </div>
    </div>
    <div class="box">
      <div class="form">
        <h1>Add Product</h1>
        <div class="input_form">
          <label class="label">Product Name</label>
          <input
            class="field_input"
            v-model="R_P_name"
            placeholder="Product Name" />
          <label class="label">Unit</label>
          <input class="field_input" v-model="R_Unit" placeholder="Unit" />
          <label class="label">Quantity</label>
          <input class="field_input" v-model="R_Qut" placeholder="Quantity" />
          <label class="label">Price</label>
          <input class="field_input" v-model="R_price" placeholder="Price" />
          <label class="label">Mfg-Date</label>
          <input
            class="field_input"
            v-model="R_MFG"
            placeholder="Mfg-Date"
            type="date" />
          <label class="label">Exp-Date</label>
          <input
            class="field_input"
            v-model="R_Exp"
            placeholder="Exp-Date"
            type="date" />
          <!-- <input class="field_input" v-model="R_image" placeholder="R_image" /> -->
          <label class="label">Select Category</label>
          <select class="field_input" v-model="R_C_id">
            <option disabled value="">Select Category</option>
            <option
              v-for="sec in datacategory"
              :key="sec"
              :value="sec.Category_id">
              {{ sec.Categoryname }}
            </option>
          </select>
          <div>
            <button
              id="upload_widget"
              v-on:click="upload_widget"
              class="cloudinary-button">
              Upload Image
            </button>
          </div>
          <div class="error">{{ error }}</div>
          <button class="login-btn" v-on:click="requestProduct">Add</button>
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
  width: 95%;
  box-sizing: border-box;
} */
.field_input {
  width: 100%;
  padding: 5px 10px;
  /* height: 30px; */
  margin-bottom: 10px;
  border: 1px solid lightgray;
  border-radius: 5px;
  outline: none;
  transition-duration: 5ms;
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
