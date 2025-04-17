<script >
import axios from 'axios';

export default{

  data() {
    return{
      datacategory:[],
      dataproduct:[]
    }
  },
  methods:{
   datacate() {
      axios.get('http://127.0.0.1:5000/category').then(response => {
      console.log(response)
      this.datacategory = response.data
    }),
    console.log("Category")
   },
   dataprod() {
      axios.get('http://127.0.0.1:5000//Products').then(response => {
      console.log(response)
      this.dataproduct = response.data
    }),
    console.log("products")
   }  
  },

  mounted() {
        this.datacate();
        this.dataprod();
        
    }



}

</script>

<template>
  <div>
    <!-- <p>{{this.datacategory}}</p> -->
    <!-- <p>{{this.dataproduct}}</p> -->

  </div>
</template>