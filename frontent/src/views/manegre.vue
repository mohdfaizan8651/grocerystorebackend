<script>
import axios from "axios";
import { RouterLink, RouterView } from "vue-router";

export default {
  data() {
    return {
      datacategory: [],
      dataproduct: [],
    };
  },
  methods: {
    datacate() {
      const token = sessionStorage.getItem("user");
      axios
        .get("http://127.0.0.1:5000/category/manager", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          this.datacategory = response.data;
        })
        .catch((error) => {
          console.error("Error fetching category", error); // Handle potential errors
        });
      console.log("Category", this.datacategory);
    },
    dataprod() {
      axios.get("http://127.0.0.1:5000//Products").then((response) => {
        console.log(response);
        this.dataproduct = response.data;
      }),
        console.log("products");
    },

    deletprod(prod) {
      alert("Faizan Carefully", prod);
      console.log("nice", prod.Category_id);
      const token = sessionStorage.getItem("user");
      if (token) {
        console.log(token);
        axios({
          url: "http://127.0.0.1:5000/requestProduct",
          method: "POST",
          data: {
            R_C_id: prod.Category_id,
            R_P_id: prod.Product_id,
            R_P_name: prod.Productname,
            R_Unit: prod.Unit,
            R_Qut: prod.Qut,
            R_price: prod.price,
            R_MFG: prod.MFG,
            R_Exp: prod.Exp,
            R_image: prod.image,
            R_P_type: "DELETE",
          },

          headers: {
            "Content-Type": "application/json",
            "Authorization ": `Bearer ${token}`,
          },
          // 20/05/2024
        })
          .then((response) => {
            alert(response.data);

            console.log(" After Api Success prduct");
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    deletcats(cate) {
      const token = sessionStorage.getItem("user");

      axios({
        url: "http://127.0.0.1:5000/categoryProduct",
        method: "POST",
        data: {
          R_C_name: cate.Categoryname,
          R_C_type: "DELETE",
        },
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
        .then((response) => {
          alert("Request Delete");
        })
        .catch((error) => {
          console.log(error);
        });
      console.log(cate, "Faizan");
    },
    filterProduct(Category_id) {
      return this.dataproduct.filter(
        (prod) => prod.Category_id === Category_id
      );
    },
  },

  mounted() {
    this.datacate();
    this.dataprod();
  },
};
</script>

<template>
  <div>
    <h2>Manager</h2>
    <div>
      <div v-for="cate in datacategory" :key="cate.Category_id">
        <div class="cat-name">
          <p class="me-2">{{ cate.Categoryname }}</p>
          <span @click="deletcats(cate)"
            ><i class="bi bi-trash-fill fs-3"></i
          ></span>
        </div>

        <div class="prods">
          <div
            class="prod"
            v-for="pods in filterProduct(cate.Category_id)"
            :key="pods.Category_id">
            <!-- <img
              style="width: 100%; border-radius: 3px; height: 200px"
              src="C:\Users\MOHD AMAN\Desktop\faizan_project\backend\static\images\thought-catalog-9aOswReDKPo-unsplash.jpg"
              alt="" /> -->
            <img
              :src="pods.image"
              alt="Product Image"
              style="width: 100%; border-radius: 3px; height: 200px" />

            <div>
              <p class="text-center fs-5">{{ pods.Productname }}</p>
              <p>Qnt: {{ pods.Qut }}</p>
              <p>Rs: {{ pods.price }}/{{ pods.Unit }}</p>
              <p>Mfg date: {{ pods.MFG }}</p>
              <p>Exp date: {{ pods.Exp }}</p>
              <button class="delete-btn" @click="deletprod(pods)">
                Delete
              </button>
            </div>
            <!--  {{ pods.Category_id }} -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h2 {
  text-align: center;
}
.cat-name {
  /* text-align: center; */
  font-size: 26px;
  margin-bottom: 10px;
  display: flex;
  justify-content: center;
}
.prods {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  /* gap: 10px; */
  align-items: center;
  min-height: 100px;
  justify-content: start;
}

.prod {
  min-width: 150px;
  height: auto;
  padding: 10px;
  gap: 10px;
  transition: 0.3s ease-in-out;
}
.prod:hover {
  box-shadow: 2px 5px 10px 2px rgba(0, 0, 0, 0.1);
}
.prod-name {
  text-align: center;
  font-size: 20px;
}
/* .price,.exp{

} */
.delete-btn {
  width: 100%;
  padding: 6px;
  border-radius: 3px;
  border: none;
  cursor: pointer;
  background-color: seagreen;
  color: white;
  transition: 0.3s;
}
.delete-btn:hover {
  background-color: rgb(58, 160, 102);
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}

.wrapper {
  height: 40px;
}
</style>
