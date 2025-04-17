
// Vue.component("singin", {

//     template: `
//     <div>
//     <!-- Button trigger modal -->
//       <label  for="singin1">Sigin</label>
//     <button type="button" id="singin1" style="display: none;" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#signin">
    
//     </button>

// <!-- Modal -->
// <div class="modal fade"  id="signin" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
// <div class="modal-dialog">
// <div class="modal-content">
// <div class="modal-header">
//   <h2 style="margin-left: 41%;"  class="modal-title" id="exampleModalLabel">Sigin </h2>
//   <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
// </div>
// <div  class="modal-body">
// <p>Username</p>
//   <input type="text" class="input" v-model="username" placeholder="Enter Email"><br><br>
//   <p>Password</p>
//   <input type="password" class="input" v-model="password" placeholder="Password"><br>
//   <div class="form-check">
//         <input class="form-check-input" type="radio"  value="maneger"    v-model="Role"    name="flexRadioDefault" id="flexRadioDefault1">
//         <label class="form-check-label" for="flexRadioDefault1">
//           Maneger
//         </label>
//       </div>
//       <div class="form-check">
//         <input class="form-check-input" type="radio"  value="user" v-model="Role"    name="flexRadioDefault" id="flexRadioDefault2" checked>
//         <label class="form-check-label" for="flexRadioDefault2">
//           User
//         </label>
//       </div>
//     <div class="form-check">

// </div>
// <div class="modal-footer">
//   <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
//   <button type="button" @click="ragister()" data-bs-dismiss="modal"class="btn btn-primary">Login</button>
// </div>
// </div>
// </div>
// </div>
// </div> 
// </div>            
//   `,
//     data() {
//       return {
  
//         username: '',
//         password: '',
//         Role: '',
  
  
//       }
//     },
//     methods: {
//       async ragister() {
//         console.log("Details", this.username, this.password, this.Role)
  
//         data_api = await fetch('http://127.0.0.1:5000/api/userragister', {
//           method: "POST", headers: { 'content-type': 'application/json' },
//           body: JSON.stringify({ "Username": this.username, "Password": this.password, "Role": this.Role })
//         });
  
//         val = await data_api.json()
//         if (val.message == "Ragister successfully") {
//           console.log("Go head", val)
//           this.username = ''
//           this.password = ''
//           alert(val.message)
  
  
//         } else {
//           console.log('check condition', val)
//           this.username = ''
//           this.password = ''
//           alert(val.message)
  
//         }
  
  
//       },
  
  
//     },
//   })
  
  // Vue.component("Login", {
  //   template: `<div>
  // <!-- Button trigger modal -->
  //   <label id='label_id' for="login">Login</label>
  // <button type="button" id="login" style="display: none;" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#Loginpage">
  
  // </button>
  
  // <!-- Modal -->
  // <div class="modal fade" id="Loginpage" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  // <div class="modal-dialog">
  // <div class="modal-content">
  //   <div class="modal-header">
  //     <h2 style="margin-left: 41%;" class="modal-title" id="exampleModalLabel">Login </h2>
  //     <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
  //   </div>
  //   <div  class="modal-body">
  //     <p>Username</p>
  //     <input type="text" class="input" v-model="username" placeholder="Enter Email"><br><br>
  //     <p>Password</p>
  //     <input type="password"class="input" v-model="password" placeholder="Password"><br>
  
  //   </div>
  //   <div class="modal-footer">
  //     <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
  //     <button type="button" @click="Login()" data-bs-dismiss="modal"class="btn btn-primary">Login</button>
  //   </div>
  // </div>
  // </div>
  // </div>
  
  // </div>`,
  //   data() {
  //     return {
  //       username: '',
  //       password: '',
        
  //     }
  //   },
  //   methods: {
  //     async Login() {
  //       console.log("Details", this.username, this.password, this.Role)
  
  //       data_api = await fetch('http://127.0.0.1:5000/api/userLogin', {
  //         method: "POST", headers: { 'content-type': 'application/json' },
  //         body: JSON.stringify({ "Username": this.username, "Password": this.password })
  //       });
  
  //       val = await data_api.json()
  //       if (val.message == "Login successfully") {
  //         console.log("Go head", val
  //         )
  //         localStorage.setItem("token", val.token)
  //         document.getElementById("label_id").style.display = 'None';
  //         document.getElementById("Logout").style.display = 'block';
  //         this.username = '',
  //           this.password = ''
  
  //         // this.$router.push({ path: '/home'})
  
  //       } else {
  //         console.log('check condition', val)
  
  //         alert(val.message)
  //       }
  
  
  //     }
  
  //   },
  //   mounted() {
  //     token = localStorage.getItem("token")
  
  //     if (token) {
  //       alert("already logged in")
  //       document.getElementById("label_id").style.display = 'None';
  //       document.getElementById("Logout").style.display = 'block';
  //       document.getElementById("usernaem").style.display = 'block';
  //       // document.getElementById("username").innerHTML = token.Username;
  
  
  //       // this.$router.push({ path: '/home'})
  //     } else {
  //       document.getElementById("label_id").style.display = 'block';
  //       document.getElementById("Logout").style.display = 'None';
  //       // document.getElementById("username").innerHTML = None;
  //     }
  
  //   }
  // })  




const card=new Vue({
    el: '#app',
    delimiters: ['{(', ')}'],
    data(){
        return{
            Products:[],
            N_prod:0,
            total: 0,
            search_cat: '',
            search_category: [],
            emailid:'',
            upiid:''
        }
    },
    mounted(){

        this.total_pord()
    },
    methods:{
   
    
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
                // total=localStorage.getItem("total")

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
      async decrease(index,prod) {
        // return this.counter++
        data_prod_api = await fetch('http://127.0.0.1:5000/api/product', {
                method: "put", headers: { 'content-type': 'application/json' },
                body: JSON.stringify({ "id":prod.Product_id, "name":prod.Productname , "qnt":prod.Product_Unit, "exp_date":prod.ProductExp, "price":prod.price,
                 "nop":prod.Product_Qut+1, "image":prod.image, "cate_id":prod.Category_id })
            });

        this.Products.splice(index, 1);
        let data2 = JSON.stringify(this.Products)
        localStorage.setItem("Prod_Card",data2)
        total=localStorage.getItem("total")

        this.total=Number(this.total)-Number(prod.price);
        localStorage.setItem("total",this.total)

        document.getElementById(prod.Product_id).disabled = false;

        console.log("Success local Storage")
      },
      total_pord(){
        countProd=localStorage.getItem("Prod_Card")
        this.Products =JSON.parse(countProd)
        this.search_category = JSON.parse(countProd);

        this.total=localStorage.getItem("total")
      
      },
      search() {
        let search_get_cetegory = [];
        this.search_category = this.Products;
        console.log(this.search_cat, this.Products)
        for (let i = 0; i < this.Products.length; i++) {
          const cates = this.Products[i]["Productname"].toLowerCase()
          const ser = this.search_cat.toLowerCase()
          if (cates.includes(ser)) {
            search_get_cetegory.push(this.Products[i])
            // console.log(cates)
  
          }
        }
        console.log(search_get_cetegory)
        // Vue.set(this.get_cetegory, []);
        this.search_category = search_get_cetegory;
  
      },
      async buy(){
        token=localStorage.getItem("token")
            console.log(token)

        if(token){
            countProd=localStorage.getItem("Prod_Card")
            buy_prod =JSON.parse(countProd)

            data_prod_api = await fetch('http://127.0.0.1:5000/api/buyproduct', {
                method: "POST", headers: { 'content-type': 'application/json' },
                body: JSON.stringify({ "Buy_product": buy_prod,"username":this.emailid})
            });
            val = await data_prod_api.json()
            console.log(this.emailid,val)

            if (val.message== 'Payment success'){
                alert(val.message)
            }else{
                alert("Try again payment")
            }
            
            // const routes = [{ path: 'http://127.0.0.1:5000/', redirect: { name: 'card/payment' } }]
            console.log(buy_prod)
        }else{
          alert("You need to login")
          window.location.href = "http://127.0.0.1:5000/home";

        }
       
      }
    }
    
      
})


