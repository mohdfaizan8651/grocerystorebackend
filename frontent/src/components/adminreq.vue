<template>
  <div>
    <h3 class="text-center my-4">Category Requests</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Type</th>
          <th scope="col">User_Id</th>
          <th scope="col">Date</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="req in approvedCategoryRequests()" :key="req">
          <td>{{ req.R_C_name }}</td>
          <td>{{ req.R_C_type }}</td>
          <td>{{ req.R_user_id }}</td>
          <td>{{ req.datetime }}</td>
          <td>
            <button
              class="approve-btn"
              v-on:click="approved(req.R_id, 'category')">
              Approve
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <hr />
    <h3 class="text-center my-4">Product Requests</h3>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Type</th>
          <th scope="col">User_Id</th>
          <th scope="col">Date</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="req in approvedProductRequests()" :key="req">
          <td>{{ req.R_P_name }}</td>
          <td>{{ req.R_P_type }}</td>
          <td>{{ req.R_user_id }}</td>
          <td>{{ req.datetime }}</td>
          <td>
            <button
              class="approve-btn"
              v-on:click="approved(req.R_id, 'product')">
              Approve
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<style>
.approve-btn {
  border: none;
  outline: none;
  background: seagreen;
  border-radius: 5px;
  padding: 5px 16px;
  color: white;
  transition: 0.3s;
}
.approve-btn:hover {
  background-color: rgb(58, 160, 102);
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}
</style>
<script>
import axios from "axios";

import { mapGetters } from "vuex";

export default {
  data() {
    return {
      reqProd: [],
      reqCate: [],
      user: "",
    };
  },
  methods: {
    approvedCategoryRequests() {
      return this.reqCate.filter((req) => req.R_approved == 0);
    },
    approvedProductRequests() {
      return this.reqProd.filter((req) => req.R_approved == 0);
    },
    reqCategory() {
      const token = sessionStorage.getItem("user");
      axios({
        url: "http://127.0.0.1:5000/categoryProduct",
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Authorization ": `Bearer ${token}`,
        },
      })
        .then((response) => {
          this.reqCate = response.data;
          console.log("Check This Faizan",this.reqCate)
        
        })
        .catch((error) => {
          console.log(error);
        });
    },

    reqproduct() {
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
          this.reqProd = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    approved(R_id, type) {
      const token = sessionStorage.getItem("user");

      if (type == "product") {
        axios({
          url: "http://127.0.0.1:5000/requestProduct",
          method: "PUT",
          data: {
            R_id: R_id,
          },
          headers: {
            "Content-Type": "application/json",
            "Authorization ": `Bearer ${token}`,
          },
        })
          .then((response) => {
            this.reqProd = response.data;
            alert("Approved");
            this.reqproduct();
            console.log(" After Api Approved prduct");
          })
          .catch((error) => {
            console.log(error);
          });
      } else if (type == "category") {
        axios({
          url: "http://127.0.0.1:5000/categoryProduct",
          method: "PUT",
          data: {
            R_id: R_id,
          },
          headers: {
            "Content-Type": "application/json",
            "Authorization ": `Bearer ${token}`,
          },
        })
          .then((response) => {
            this.reqProd = response.data;
            this.reqCategory();
            alert("Approved", "category");
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
  mounted() {
    this.reqproduct(), 
    this.reqCategory();
    
  },
};
</script>
