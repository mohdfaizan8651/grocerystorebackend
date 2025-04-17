<script>
import { cartoonify } from "@cloudinary/url-gen/actions/effect";
import { none } from "@cloudinary/url-gen/qualifiers/progressive";
import axios from "axios";
import { RouterLink, RouterView } from "vue-router";

export default {
  computed: {
    onSearch() {
      if (this.query != "") {
        this.dataproduct = this.searchprod.filter((dataproduct) =>
          dataproduct.product_name
            .toLowerCase()
            .includes(this.query.toLowerCase())
        );
        console.log(this.query, this.dataproduct);
      } else if (this.query == "") {
        this.dataproduct = this.searchprod;
      }
    },
  },

  data() {
    return {
      dataproduct: [],

      searchprod: [],
      query: "",
      cart: [],
    };
  },

  methods: {
    grandTotal() {
      let total = 0;
      for (let prod of this.dataproduct) {
        total += prod.total_price;
      }
      return total;
    },
    dataprod() {
      const token = sessionStorage.getItem("user");
      axios
        .get("http://127.0.0.1:5000/cart", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          console.log(response);
          this.dataproduct = response.data.cart_items;
          this.searchprod = this.dataproduct;
          console.log("Faizan prod", this.searchprod);
        }),
        console.log("products", this.dataproduct);
    },

    addproduct(prod) {
      const token = sessionStorage.getItem("user");

      axios({
        method: "POST",
        url: "http://127.0.0.1:5000/cart",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        data: {
          email_id: this.emailid,
          product_id: prod.product_id,
          quentity: 1,
        },
      }).then((response) => {
        this.dataprod();
        console.log(response.data);
      });
    },
    deleteproduct(prod) {
      const token = sessionStorage.getItem("user");

      axios({
        method: "PUT",
        url: `http://127.0.0.1:5000/cart/${prod.cart_item_id}`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }).then((response) => {
        this.dataprod();
        console.log(response.data);
      });
    },
  },
  mounted() {
    this.dataprod();
  },
};
</script>

<template>
  <div>
    <div class="search-component">
      <input type="text" v-model="query" @input="onSearch" placeholder="Search..." />
    </div>
    <RouterView />
    <h2>Cart</h2>
    <hr />

    <div v-for="prods in dataproduct" :key="prods.Product_id">
      <div class="item">
        <div>
          <!-- <img
            src="C:\Users\MOHD AMAN\Desktop\faizan_project\backend\static\images\thought-catalog-9aOswReDKPo-unsplash.jpg"
            alt="" /> -->
          <img :src="prods.product_image" alt="Product Image" />
        </div>
        <div id="prod-name">{{ prods.product_name }}</div>
        <div id="price">{{ prods.price }}</div>
        <div class="action">
          <button class="action-btn" v-on:click="deleteproduct(prods)">
            -
          </button>
          <span class="quantity">{{ prods.quantity }}</span>
          <button class="action-btn" v-on:click="addproduct(prods)">+</button>
        </div>
      </div>
    </div>
    <hr />
    <h1 class="total">Grand Total : {{ grandTotal() }}</h1>
  </div>
</template>

<style scoped>
.wrapper {
  height: 40px;
}

.total {
  display: flex;
  justify-content: center;
  margin: 40px 0px;
}

h2 {
  text-align: center;
}

.item {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin: 10px;
}

.item img {
  width: 50px;
  height: 50px;
  border-radius: 20px;
}

.item #prod-name,
#price {
  font-size: 20px;
  text-align: start;
}

.item .action .action-btn {
  background: seagreen;
  border: none;
  width: 25px;
  height: 25px;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  transition-delay: 5ms;
}

.item .action .action-btn:hover {
  scale: 0.95;
  background-color: rgb(58, 160, 102);
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}

.item .action .quantity {
  margin: 0px 10px;
  font-weight: bolder;
}
</style>
