
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAVW3oI-FNZcwgX-mUQGtezKFyhljWmYCM",
  authDomain: "test-83810.firebaseapp.com",
  databaseURL: "https://test-83810-default-rtdb.firebaseio.com",
  projectId: "test-83810",
  storageBucket: "test-83810.appspot.com",
  messagingSenderId: "868604879259",
  appId: "1:868604879259:web:14e69794744f23232a813e",
  measurementId: "G-0SH0K2FN18"
};

// Initialize Firebase
if (window.firebase && window.firebase.initializeApp) {
   firebase= firebase.initializeApp(firebaseConfig);
  // var database=firebase.database()
  // console.log(database)
}




// only Add category

new Vue({
  el: '#Addcategory',
  delimiters: ['{(', ')}'],
  data: {
    value_category: '',
    get_cetegory: [],

  },
  methods: {


    // fetch api funtion for add category

    async R_addCategory(Username,userid) {
      Token=localStorage.getItem("token")

      // Request to Admin for adding a category
      data_api = await fetch('http://127.0.0.1:5000//testimonial', {
        method: "POST", headers: { 'content-type': 'application/json','Authorization': `Bearer ${Token}` },
        
        body: JSON.stringify({"request":"Add Category","R_Category_name":this.value_category})
      });

      val = await data_api.json()

      
      console.log("panding Add category",val)
      
      alert("panding Add category",val)


      // data_api = await fetch('http://127.0.0.1:5000//testimonial', {
      //   method: "get", headers: { 'content-type': 'application/json','Authorization': `Bearer ${Token}` },
        
      //   body: JSON.stringify()
      // });

      // val = await data_api.json()
      // console.log(val,val["testimonials"].length)

      // // for(i=0;i<val["testimonials"].length;i++){
      // //   if(val["testimonials"][i]["username"]==Username){
      // //     console.log(val["testimonials"][i]["content"])
      // //   }else {
      // //     console.log(Username,"No pandding request")
      // //   }
        

      // // }


      // this.value_category = ""

      // // Add category 
      // data_api = await fetch('http://127.0.0.1:5000/api/category', {
      //   method: "POST", headers: { 'content-type': 'application/json' },
      //   body: JSON.stringify({ "name": this.value_category, "user_id": user_id })
      // });

      // val = await data_api.json()

      // console.log("after Add new Category", val);
      // this.value_category = ""

    },
  },

})














Vue.component("singin", {

  template: `
  <div>
        <!-- Button trigger modal -->
          <label  for="singin1">Sigin</label>
        <button type="button" id="singin1" style="display: none;" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#signin">
        
        </button>
  
  <!-- Modal -->
  <div class="modal fade" id="signin" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
  <div class="modal-content">
    <div class="modal-header">
      <h2 style="margin-left: 41%;"  class="modal-title" id="exampleModalLabel">Sigin </h2>
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div  class="modal-body">
    <p>Username</p>
      <input type="text" class="input" v-model="username" placeholder="Enter Email"><br><br>
      <p>Password</p>
      <input type="password" class="input" v-model="password" placeholder="Password"><br>
      <div class="form-check">
            <input class="form-check-input" type="radio"  value="maneger"    v-model="Role"    name="flexRadioDefault" id="flexRadioDefault1">
            <label class="form-check-label" for="flexRadioDefault1">
              Maneger
            </label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio"  value="user" v-model="Role"    name="flexRadioDefault" id="flexRadioDefault2" checked>
            <label class="form-check-label" for="flexRadioDefault2">
              User
            </label>
          </div>
        <div class="form-check">

    </div>
    <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      <button type="button" @click="ragister()" data-bs-dismiss="modal"class="btn btn-primary">Login</button>
    </div>
  </div>
  </div>
  </div>
 </div> 
</div>       
`,
  data() {
    return {

      username: '',
      password: '',
      Role: '',


    }
  },
  methods: {
    async ragister() {
      console.log("Details", this.username, this.password, this.Role)

      data_api = await fetch('http://127.0.0.1:5000/api/userragister', {
        method: "POST", headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ "Username": this.username, "Password": this.password, "Role": this.Role })
      });

      val = await data_api.json()
      if (val.message == "Ragister successfully") {
        console.log("Go head", val)
        this.username = ''
        this.password = ''
        alert(val.message)


      } else {
        console.log('check condition', val)
        this.username = ''
        this.password = ''
        alert(val.message)

      }


    },


  },
})







Vue.component("Login", {
  template: `<div>
<!-- Button trigger modal -->
  <label id='label_id' for="login">Login</label>
<button type="button" id="login" style="display: none;" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#Loginpage">

</button>

<!-- Modal -->
<div class="modal fade" id="Loginpage" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
<div class="modal-dialog">
<div class="modal-content">
  <div class="modal-header">
    <h2 style="margin-left: 41%;" class="modal-title" id="exampleModalLabel">Login </h2>
    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
  </div>
  <div  class="modal-body">
    <p>Username</p>
    <input type="text" class="input" v-model="username" placeholder="Enter Email"><br><br>
    <p>Password</p>
    <input type="password"class="input" v-model="password" placeholder="Password"><br>

  </div>
  <div class="modal-footer">
    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
    <button type="button" @click="Login()" data-bs-dismiss="modal"class="btn btn-primary">Login</button>
  </div>
</div>
</div>
</div>

</div>`,
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async Login() {
      console.log("Details", this.username, this.password, this.Role)

      data_api = await fetch('http://127.0.0.1:5000/api/userLogin', {
        method: "POST", headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ "Username": this.username, "Password": this.password })
      });

      val = await data_api.json()
      if (val.message == "Login successfully") {
        console.log("Go head", val
        )
        localStorage.setItem("token", val.token)
        document.getElementById("label_id").style.display = 'None';
        document.getElementById("Logout").style.display = 'block';
        this.username = '',
          this.password = ''

        // this.$router.push({ path: '/home'})

      } else {
        console.log('check condition', val)

        alert(val.message)
      }


    }

  },
  mounted() {
    token = localStorage.getItem("token")

    if (token) {
      alert("already logged in")
      document.getElementById("label_id").style.display = 'None';
      document.getElementById("Logout").style.display = 'block';
      document.getElementById("usernaem").style.display = 'block';
      // document.getElementById("username").innerHTML = token.Username;


      // this.$router.push({ path: '/home'})
    } else {
      document.getElementById("label_id").style.display = 'block';
      document.getElementById("Logout").style.display = 'None';
      // document.getElementById("username").innerHTML = None;
    }

  }
})


























// Edit Product 
const EditProductModel = Vue.component("modal", {
  props: ['Category_id', 'Product_id'],
  template: `
<div >
    <!-- Modal1 -->
    <div class="modal fade" id="editproductModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          
          <div class="modal-body">
          <input type="text" v-model="Productname" placeholder="New Productname">
          <input type="text" v-model="Product_Unit" placeholder=" New Product_Unit">
          <label class="form-label" for="customFile">Default file input example</label>
          <input type="file"  @change="handleFileUpload" class="form-control" id="customFile" />
          <input type="date" v-model="ProductExp" placeholder="New ProductExp">
          <input type="type" v-model="price" placeholder="New price">
          <input type="Integer" v-model="Product_Qut" placeholder="New Product_Qut">
          
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" @click="editproduct( $route.params.Category_id ,$route.params.Product_id )"  data-bs-dismiss="modal">Edit Save</button>
            
            </div>
        </div>
      </div>
    </div>
</div>       
`,
  data() {
    return {
      Productname: '',
      Product_Unit: '',
      image: '',
      ProductExp: '',
      price: '',
      Product_Qut: null,

    }
  },
  methods: {

    async editproduct(cateid, prodid) {
      console.log("Edit Product", this.Productname, this.Product_Unit, this.image, this.ProductExp, this.price, this.Product_Qut, cateid, prodid);

      data_api = await fetch('http://127.0.0.1:5000/testimonial', {
        method: "post", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

        body: JSON.stringify({"request":"Edit Product","Product_id":prodid ,"name": this.Productname, "qnt": this.Product_Unit, "exp_date": this.ProductExp, "price": this.price, "nop": this.Product_Qut, "image": this.image, "cate_id": cateid })
    });

    val = await data_api.json()
    console.log(val)
    alert("Request to Admin", val)


      // data_api = await fetch('http://127.0.0.1:5000/api/product', {
      //   method: "PUT", headers: { 'content-type': 'application/json' },
      //   body: JSON.stringify({ "id": prodid, "name": this.Productname, "qnt": this.Product_Unit, "exp_date": this.ProductExp, "price": this.price, "nop": this.Product_Qut, "image": this.image, "cate_id": cateid })
      // });

      // val = await data_api.json()

      console.log("after  Add Product", val, cateid, prodid);
      this.Productname = '',
        this.Product_Unit = '',
        this.image = '',
        this.ProductExp = '',
        this.price = '',
        this.Product_Qut = null

    },
    handleFileUpload(e) {

      var file = e.target.files[0];
      //Create a storage ref
      const fileName = `${Date.now()}-${file.name}`
      const storageRef = firebase.storage().ref("images/" + fileName);
      console.log(storageRef, "storageRef")
      /** folder name will be email, 
      // Will have to transfer variable from page to page and files will be .jpeg**/
      //Upload file 

      let task = storageRef.put(file);
      //Update progress bar
      this.image = `https://firebasestorage.googleapis.com/v0/b/test-83810.appspot.com/o/images%2F${fileName}?alt=media`;

      task.on('state_changed',
        function progress(snapshot) {
          console.log(snapshot, "snapshot")
        }, (error) => {
          console.log(error, "error")
        },
        function complete(url) {
          console.log(`https://firebasestorage.googleapis.com/v0/b/test-83810.appspot.com/o/images%2F${fileName}?alt=media`)
        });



    }



  }




})






// product Add componenet
const ProductModel = Vue.component("modal1", {
  props: ['id'],
  template: `
<div >
    <!-- Modal1 -->
    <div class="modal fade" id="productModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          
          <div class="modal-body">
          <input type="text" v-model="Productname" placeholder="Productname">
          <input type="text" v-model="Product_Unit" placeholder="Product_Unit">
          <label class="form-label" for="customFile">Default file input example</label>
          <input type="file"  @change="handleFileUpload" class="form-control" id="customFile" />
          <input type="date" v-model="ProductExp" placeholder="ProductExp">
          <input type="type" v-model="price" placeholder="price">
          <input type="Integer" v-model="Product_Qut" placeholder="Product_Qut">
          
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" @click="addproduct( $route.params.id )"  data-bs-dismiss="modal">Save</button>
            
            </div>
        </div>
      </div>
    </div>
</div>       
`,
  data() {
    return {
      Productname: '',
      Product_Unit: '',
      image: '',
      ProductExp: '',
      price: '',
      Product_Qut: 0,

    }
  },
  methods: {

    async addproduct(cateid) {
      console.log("Add Product", this.Productname, this.Product_Unit, this.image, this.ProductExp, this.price, this.Product_Qut);
      
      // Request to admin add Product
      data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "post", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({"request":"Add Product", "name": this.Productname, "qnt": this.Product_Unit, "exp_date": this.ProductExp, "price": this.price, "nop": this.Product_Qut, "image": this.image, "cate_id": cateid })
                });

                val = await data_api.json()
                console.log(val)
                alert("Request to Admin", val)



      // data_api = await fetch('http://127.0.0.1:5000/api/product', {
      //   method: "POST", headers: { 'content-type': 'application/json' },
      //   body: JSON.stringify({ "name": this.Productname, "qnt": this.Product_Unit, "exp_date": this.ProductExp, "price": this.price, "nop": this.Product_Qut, "image": this.image, "cate_id": cateid })
      // });

      // val = await data_api.json()

      // console.log("after  Add Product", val, cateid);
      this.Productname = '',
        this.Product_Unit = '',
        this.image = '',
        this.ProductExp = '',
        this.price = '',
        this.Product_Qut = 0

    },
    handleFileUpload(e) {

      var file = e.target.files[0];
      //Create a storage ref
      const fileName = `${Date.now()}-${file.name}`
      const storageRef = firebase.storage().ref("images/" + fileName);
      console.log(storageRef, "storageRef")
      /** folder name will be email, 
      // Will have to transfer variable from page to page and files will be .jpeg**/
      //Upload file 

      let task = storageRef.put(file);
      //Update progress bar
      this.image = `https://firebasestorage.googleapis.com/v0/b/test-83810.appspot.com/o/images%2F${fileName}?alt=media`;

      task.on('state_changed',
        function progress(snapshot) {
          console.log(snapshot, "snapshot")
        }, (error) => {
          console.log(error, "error")
        },
        function complete(url) {
          console.log(`https://firebasestorage.googleapis.com/v0/b/test-83810.appspot.com/o/images%2F${fileName}?alt=media`)
        });



    }



  }




})


const CategoryModel = Vue.component("modal", {
  props: ['id'],
  template: `
  <div >
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
          <input type="type" v-model="newcat" placeholder="Enter new Category">
          
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" @click="editcategory( $route.params.id )"  data-bs-dismiss="modal">Save</button>
            
            </div>
        </div>
      </div>
    </div>
  </div>       
`,
  data() {
    return {
      newcat: ''
    }
  },
  methods: {

    async editcategory(cateid) {
      console.log("Add Edit Category", this.newcat);
      Token=localStorage.getItem("token")
            data_api = await fetch('http://127.0.0.1:5000/testimonial', {
            method: "post", headers: { 'content-type': 'application/json','Authorization': `Bearer ${Token}` },
            
            body: JSON.stringify({"request":"Edit Category","Category_id":cateid,"Category_name":this.newcat})
          });
    
          val = await data_api.json()
          
          console.log("Request testimonial ",val)

    },



  }


})


const routes = [
  { path: '/user/Product/:id', component: ProductModel, props: true },
  { path: '/user/:id', component: CategoryModel, props: true },
  { path: '/user/Product/:Category_id/:Product_id', component: EditProductModel, props: true },
  // { path: '/card', component: card }



]

// show Category Product Add Category and Product also Edit 

const router = new VueRouter({
  routes
})


new Vue({
  el: '#S_C_P_A2_E12_D12',
  delimiters: ['{(', ')}'],
  router: router,
  data() {
    return {cartProd:0,
      get_cetegory: [],
      get_product: [],
      search_cat: '',
      search_category: [],
      Add_Category:[],
      Edit_Category:[],
      Add_Product:[],
      Edit_Product:[],
      Delete_Product:[],
      Delete_Category:[],
      Products:[],
      total: 0
      

    }
  },
  mounted() {
    this.Category()
    this.Product(),
    this.add_Cat_App(),
    this.total_pord()

  },
  methods: {


    // get getcetagory

    async Category() {
      console.log("Category");

      data_api = await fetch('http://127.0.0.1:5000/api/category', {
        method: "GET", headers: { 'content-type': 'application/json' },
        body: JSON.stringify()
      });

      val = await data_api.json()

      console.log("Category", val);
      this.get_cetegory = val;
      this.search_category = val;

      countProd=localStorage.getItem("Prod_Card")
      let Nop =JSON.parse(countProd)
      
      this.N_prod=Nop.length;
      console.log(this.N_prod)
 




    },


    // get getproduct
    async Product() {
      console.log("Product");
      
      

      data_api = await fetch('http://127.0.0.1:5000/api/product', {
        method: "GET", headers: { 'content-type': 'application/json' },
        body: JSON.stringify()
      });

      val = await data_api.json()

      console.log("Product", val);
      this.get_product = val;

    },
    
    async addItem(prod) {
      data_api = await fetch('http://127.0.0.1:5000/api/product', {
      method: "get", headers: { 'content-type': 'application/json' },
      body: JSON.stringify()
  });

  val = await data_api.json()
  // const findItem = val.find(val => number === 'five')

  const result = val.find(({ Product_id }) => Product_id === prod.Product_id);
  if (result.Product_Qut>=1){
      // this.Products.splice(index, 1);
      data_prod_api = await fetch('http://127.0.0.1:5000/api/product', {
          method: "put", headers: { 'content-type': 'application/json' },
          body: JSON.stringify({ "id":prod.Product_id, "name":prod.Productname , "qnt":prod.Product_Unit, "exp_date":prod.ProductExp, "price":prod.price,
           "nop":result.Product_Qut-1, "image":prod.image, "cate_id":prod.Category_id })
      });
      val = await data_prod_api.json()
      if(val.massage=="Product update successfully"){

          this.Products.push(prod);

          let data2 = JSON.stringify(this.Products)
          localStorage.setItem("Prod_Card",data2)
          this.total=Number(this.total)+Number(prod.price);
          localStorage.setItem("total",this.total)



          console.log("Success local Storage")
      }else{
          console.log("Prb in ",val.massage)
      }

  }else if(result.Product_Qut<=0){
      document.getElementById(prod.Product_id).disabled = true;
      console.log("Out of Stoke",prod)
  }
    
    console.log("addProd su",result);
},
total_pord(){
    countProd=localStorage.getItem("Prod_Card")
    console.log("card Data",countProd)


  if(countProd){
    
    countProd=localStorage.getItem("Prod_Card")

    this.Products =JSON.parse(countProd)
    this.total=localStorage.getItem("total")
    console.log(" card Data")
  }else{
    console.log("No card Data")

  }
  

},
// async Addtocard(prod,cat){
//       let list_c_p =[];
//       list_c_p.push(prod)
//       let Prod_Card =localStorage.getItem("Prod_Card");
//       // let data = JSON.stringify(prod)
//       if(Prod_Card == null){
//         // localStorage.setItem("Product",1);
//         let data = JSON.stringify(list_c_p)
//         localStorage.setItem("Prod_Card",data);
        



//       }else{
//         // count2=Number(count)+1
//         let data1 =JSON.parse(Prod_Card)
//         // let data = JSON.stringify(list_c_p)

//         new_card=list_c_p.concat(data1)
//         let data2 = JSON.stringify(new_card)

//         localStorage.setItem("Prod_Card",data2);

//         // localStorage.setItem("Product",count2);
//         // localStorage.setItem(count2,data);

//       }
    
      

//       console.log("from add product",list_c_p)

//       // data_api = await fetch('http://127.0.0.1:5000/api/cart', {
//       //   method: "post", headers: { 'content-type': 'application/json' },
//       //   body: JSON.stringify({"user_id":cat.buy_id,"id":prod.Product_id,"nop":1})
//       // });

//       // val = await data_api.json()

//       // console.log("Add Product to card", "val",prod,cat.buy_id
//       // );

//     },

    async removetocard(prod,cat){
      console.log(prod.Product_id)
      localStorage.removeItem(prod.Product_id,prod.Product_id);

      // data_api = await fetch('http://127.0.0.1:5000/api/cart', {
      //   method: "post", headers: { 'content-type': 'application/json' },
      //   body: JSON.stringify({"user_id":cat.buy_id,"id":prod.Product_id,"nop":1})
      // });

      // val = await data_api.json()

      // console.log("Add Product to card", "val",prod,cat.buy_id
      // );

    },




    // delete Category
    async deltecategory(cateid) {
      console.log("Add Delete Category", cateid);

      data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "post", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Delete Category", "Category_id":cateid })
                });

                val = await data_api.json()
                console.log(val)
                alert("Request Send to  Approved")

    //   data_api = await fetch('http://127.0.0.1:5000/api/category', {
    //     method: "DELETE", headers: { 'content-type': 'application/json' },
    //     body: JSON.stringify({ "id": cateid })
    //   });

    //   val = await data_api.json()

    //   console.log("after  Delete Category", val,);


    },

    async deleteproduct(Category_id, Product_id) {
      console.log(" Delete Product", Category_id, Product_id);
      data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "post", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Delete Product", "Product_id":Product_id })
                });

                val = await data_api.json()
                console.log(val)
                alert("Request Send to  Approved")

      // data_api = await fetch('http://127.0.0.1:5000/api/product', {
      //   method: "DELETE", headers: { 'content-type': 'application/json' },
      //   body: JSON.stringify({ "id": Product_id })
      // });

      // val = await data_api.json()

      // console.log("after  Delete Product", val,);


    },
    Logout() {
      alert("Logout")
      localStorage.removeItem("token")
      document.getElementById("Logout").style.display = 'None';
      document.getElementById("label_id").style.display = 'block';

      this.$router.push({ path: '/home'})
      




    },
    search() {
      let search_get_cetegory = [];
      this.search_category = this.get_cetegory;
      console.log(this.search_cat, this.get_cetegory.length)
      for (let i = 0; i < this.get_cetegory.length; i++) {
        const cates = this.get_cetegory[i]["Categoryname"].toLowerCase()
        const ser = this.search_cat.toLowerCase()
        if (cates.includes(ser)) {
          search_get_cetegory.push(this.get_cetegory[i])
          // console.log(cates)

        }
      }
      console.log(search_get_cetegory)
      // Vue.set(this.get_cetegory, []);
      this.search_category = search_get_cetegory;

    },
      
    async add_Cat_App(){

      Token=localStorage.getItem("token")
      // this.cartProd = localStorage.getItem("Product")
      if(Token){

      data_api = await fetch('http://127.0.0.1:5000/testimonial', {
        method: "get", headers: { 'content-type': 'application/json','Authorization': `Bearer ${Token}` },
        
        body: JSON.stringify()
      });

      val = await data_api.json()
      // key;
      console.log("Request testimonial ",val)
      if(val["AddCategory"].length!=0){
      for (i=0;i<=val["AddCategory"].length-1;i++){
        if (val["AddCategory"][i]["R_approved"]==false){
          // // Add category 
          // console.log(val["AddCategory"][i]["R_approved"])

          // // add category when request have approved
          this.Add_Category.push(val["AddCategory"][i])

        }

      }
    }
      console.log(this.Add_Category)

   


      console.log("Request",val["EditCategory"].length-1)
      for (i=0;i<=val["EditCategory"].length-1;i++){
        if(val["EditCategory"][i]["R_approved"]==false){
          
         this.Edit_Category.push(val["EditCategory"][i])
          

        }
        
      }
      console.log("Request",val["EditProduct"].length-1)
      for (i=0;i<=val["EditProduct"].length-1;i++){
        if (val["EditProduct"][i]["R_approved"]==false){
        this.Edit_Product.push(val["EditProduct"][i])

        }

        
      }
      console.log("Add Product Request",val["AddProduct"].length-1)
      for (i=0;i<=val["AddProduct"].length-1;i++){
        if(val["AddProduct"][i]["R_approved"]==false){
          
        this.Add_Product.push(val["AddProduct"][i])
          
           
 
         }
        
      }

      console.log("Delete Product Request",val)
      for (i=0;i<=val["DeleteProduct"].length-1;i++){
        if(val["DeleteProduct"][i]["R_approved"]==false){
          
        this.Delete_Product.push(val["DeleteProduct"][i])
          
           
 
         }
        
      }

      console.log("Delete Category Request",val["DeleteCategory"].length-1)
      for (i=0;i<=val["DeleteCategory"].length-1;i++){
        if(val["DeleteCategory"][i]["R_approved"]==false){
          
        this.Delete_Category.push(val["DeleteCategory"][i])
          
           
 
         }
        
      }
      console.log("Delete Product nd Category Request",this.Delete_Category,val["DeleteCategory"])


      }else{
        console.log("not login")
      }
      



     }
          
          
}
  },



)





// #card component
// Vue.use(Vuex)

//  new Vuex.Store({
//   state: {
//     products: [
//       { id: 1, name: 'Product A', price: 10 },
//       { id: 2, name: 'Product B', price: 20 },
//       { id: 3, name: 'Product C', price: 30 }
//     ],
//     cart: []
//   },})



  