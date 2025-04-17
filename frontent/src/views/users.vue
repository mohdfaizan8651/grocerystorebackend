<script>
import { cartoonify } from "@cloudinary/url-gen/actions/effect";
import { none } from "@cloudinary/url-gen/qualifiers/progressive";
import axios from "axios";
import { RouterLink, RouterView } from "vue-router";

export default {
  computed: {
    onSearch() {
      if (this.query != "") {
        this.datacategory = this.searchcat.filter((datacategory) =>
          datacategory.Categoryname.toLowerCase().includes(
            this.query.toLowerCase()
          )
        );

        this.dataproduct = this.searchprod.filter((dataproduct) =>
          dataproduct.Productname.toLowerCase().includes(
            this.query.toLowerCase()
          )
        );
        if (this.datacategory != []) {
          for (let i = 0; i < this.datacategory.length; i++) {
            let prods = this.searchprod.filter(
              (dataproduct) =>
                dataproduct.Category_id === this.datacategory[i].Category_id
            );

            if (
              String(
                this.dataproduct.filter(
                  (datacat) =>
                    datacat.Category_id === this.datacategory[i].Category_id
                )
              ) == []
            ) {
              this.dataproduct = this.dataproduct.concat(prods);
            }
          }
        }
        if (this.dataproduct != []) {
          for (let i = 0; i < this.dataproduct.length; i++) {
            let cate_ = this.searchcat.filter(
              (datacat) =>
                datacat.Category_id === this.dataproduct[i].Category_id
            );

            if (
              String(
                this.datacategory.filter(
                  (datacat) =>
                    datacat.Categoryname === this.dataproduct[i].Categoryname
                )
              ) == []
            ) {
              this.datacategory = this.datacategory.concat(cate_);
            } else {
              console.log(
                "Checkoutput",
                this.datacategory.filter(
                  (datacat) =>
                    datacat.Category_id === this.dataproduct[i].Category_id
                )
              );
            }
          }
        }
      } else if (this.query == "") {
        this.datacategory = this.searchcat;
        this.dataproduct = this.searchprod;
      }
    },
  },

  data() {
    return {
      datacategory: [],
      dataproduct: [],
      searchcat: [],
      searchprod: [],
      query: "",
      cart: [],
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
          console.log(response.data,"FAizan CAtegory")
          this.datacategory = response.data;

          this.searchcat = this.datacategory;
          console.log("Faizan cat", this.searchcat);
        })
        .catch((error) => {
          console.error("Error fetching category", error);
        });
    },

    dataprod() {
      axios.get("http://127.0.0.1:5000//Products").then((response) => {
        console.log(response);
        this.dataproduct = response.data;
        this.searchprod = this.dataproduct;
        console.log("Faizan prod", this.searchprod);
      }),
        console.log("products");
    },

    filterProduct(Category_id) {
      return this.dataproduct.filter(
        (prod) => prod.Category_id === Category_id
      );
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
          product_id: prod.Product_id,
          quentity: 1,
        },
      }).then((response) => {
        console.log(response.data);
        console.log(this.cart);
      });
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
    <div class="search-component">
      <input
        type="text"
        v-model="query"
        @input="onSearch"
        placeholder="Search..." />
    </div>
    <RouterView />
    <!-- <h2>User Deshboard</h2> -->
    <hr />

    <div>
      <div v-for="cats in datacategory" :key="cats.Category_id">
        <div class="cat-name category-name">{{ cats.Categoryname }}</div>

        <div class="prods">
          <div
            class="prod"
            v-for="prods in filterProduct(cats.Category_id)"
            :key="prods.Product_id">
            <img
              :src="prods.image"
              alt="Product Image"
              style="width: 100%; border-radius: 3px; height: 200px" />
            <!-- <img
              style="width: 100%; border-radius: 3px; height: 200px"
              src="C:\Users\MOHD AMAN\Desktop\faizan_project\backend\static\images\thought-catalog-9aOswReDKPo-unsplash.jpg"
              alt="" /> -->

            <div class="product">
              <p class="product-name">{{ prods.Productname }}</p>
              <p class="product-price">Rs: {{ prods.price }}/{{ prods.Unit }}</p>
              <p class="exp-date">Exp date: {{ prods.Exp }}</p>
              <button class="add-btn" v-on:click="addproduct(prods)">
                Add
              </button>
            </div>
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
  text-align: center;
  font-size: 26px;
  margin-bottom: 10px;
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
.add-btn {
  width: 100%;
  padding: 6px;
  border-radius: 3px;
  border: none;
  cursor: pointer;
  background-color: seagreen;
  color: white;
  transition: 0.3s;
}
.add-btn:hover {
  background-color: rgb(58, 160, 102);
  box-shadow: 1px 4px 8px 2px rgba(0, 0, 0, 0.1);
}

.wrapper {
  height: 40px;
}
.category-name {
    font-family: 'Pacifico', cursive;
    font-size: 36px; /* Slightly larger font for emphasis */
    background: linear-gradient(90deg, #ff7eb3, #ff758c, #ff6f61); /* Gradient text color */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent; /* Makes the gradient visible */
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Adds a subtle shadow for depth */
    letter-spacing: 2px; /* Adds spacing between letters */
    text-align: center; /* Centers the text */
    margin: 20px 0; /* Adds spacing around the category name */
  }

  .product-name {
    font-family: 'Roboto', sans-serif;
    font-size: 24px; /* Slightly larger to stand out */
    font-weight: 700; /* Bold for emphasis */
    color: #333; /* Neutral color */
    margin-bottom: 8px;
  }

  /* Product Price */
  .product-price {
    font-family: 'Merriweather', serif;
    font-size: 20px; /* Prominent but smaller than the name */
    font-weight: 600;
    color: #ff6f61; /* Attention-grabbing color */
    margin-bottom: 12px;
  }

  /* Product Description */
  .product-description {
    font-family: 'Lato', sans-serif;
    font-size: 16px;
    font-weight: 400;
    color: #555; /* Subtle color */
    line-height: 1.5; /* Increases readability */
    margin-bottom: 16px;
  }

  /* Buy Button */
  .buy-button {
    font-family: 'Open Sans', sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: white;
    background-color: #ff6f61; /* Matches price color */
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .buy-button:hover {
    background-color: #ff4c3b; /* Slightly darker on hover */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Adds depth */
  }
  .exp-date {
    font-family: 'Roboto', sans-serif; /* Clean and simple font */
    font-size: 14px; /* Small but readable */
    font-weight: 400; /* Normal weight */
    color: #555; /* Neutral gray for subtle emphasis */
    margin-top: 5px; 
  }



</style>
