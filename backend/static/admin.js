new Vue({
    el: '#testimonial',
    delimiters: ['{(', ')}'],
    data() {
        return {
            Add_Category: [],
            Edit_Category: [],
            Add_Product: [],
            Edit_Product: [],
            Delete_Product: [],
            Delete_Category: []


        }
    },
    mounted() {
        this.add_Cat_App()

    },
    methods: {
        async approved(item, cat) {
            console.log(item, cat)
            Token = localStorage.getItem("token")

            if (cat == "AddCategory") {
                data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                    method: "put", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ 'request': "Add Category", "request_id": item.R_id, "status": true })
                });

                val = await data_api.json()
                alert("Request Approved", val)
                //   add Category

                reponc_cate = await fetch('http://127.0.0.1:5000/api/category', {
                    method: "POST", headers: { 'content-type': 'application/json' },
                    body: JSON.stringify({ "name": item.R_Category_name, "user_id": item.R_user_id })
                });
                cat_responce = await reponc_cate.json()

                console.log("this time add catreger", cat_responce)

                //   Delete Request
                if (cat_responce["massage"] == 'Category add successfully') {
                    reque_resp = await fetch('http://127.0.0.1:5000/testimonial', {
                        method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                        body: JSON.stringify({ "request": "Add Category", "Add_Category_id": item.R_id })
                    });

                    responce = await reque_resp.json()
                    console.log("Delete Request", responce)
                    if (responce == null) {
                        alert("Category add successfully")
                    } else {
                        alert(responce)
                    }
                }
            } else if (cat == "EditCategory") {

                data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                    method: "put", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ 'request': "Edit Category", "request_id": item.R_id, "status": true })
                });

                val = await data_api.json()
                alert("Request Approved", val)


                // Edi Category
                reponc_cate = await fetch('http://127.0.0.1:5000/api/category', {
                    method: "put", headers: { 'content-type': 'application/json' },
                    body: JSON.stringify({ "id": item.R_Category_id, "name": item.R_Category_name, "user_id": item.R_user_id })
                });
                cat_responce = await reponc_cate.json()

                console.log("this time Edit catreger", cat_responce)

                // Dlete Request for Edit Category


                if (cat_responce["massage"] == 'Category update successfully') {
                    reque_resp = await fetch('http://127.0.0.1:5000/testimonial', {
                        method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                        body: JSON.stringify({ "request": "Edit Category", "Edit_Category_id": item.R_id })
                    });

                    responce = await reque_resp.json()
                    console.log("Delete Request", responce)
                    if (responce == null) {
                        alert("Category update successfully")
                    } else {
                        alert(responce)
                    }
                }



            } else if (cat == "AddProduct") {
                data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                    method: "put", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Add Product", "request_id": item.R_Product_id, "status": true })
                });

                val = await data_api.json()
                alert("Request Approved", val)

                data_api = await fetch('http://127.0.0.1:5000/api/product', {
                    method: "POST", headers: { 'content-type': 'application/json' },
                    body: JSON.stringify({ "name": item.R_Productname, "qnt": item.R_Product_Unit, "exp_date": item.R_ProductExp, "price": item.R_price, "nop": item.R_Product_Qut, "image": item.R_image, "cate_id": item.R_Category_id })
                });

                val = await data_api.json()

                console.log("after  Add Product", val);

                data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Add Product", "Add_Product_id": item.R_Product_id })
                });

                val = await data_api.json()
                console.log(val)
                alert("Add Product successfully", val)






            } else if (cat == "EditProduct") {

                data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                    method: "put", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Edit Product", "request_id": item.R_id, "status": true })
                });

                val = await data_api.json()
                alert("Request Approved", val)

                data_api = await fetch('http://127.0.0.1:5000/api/product', {
                    method: "PUT", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                    body: JSON.stringify({ "id": item.R_Product_id, "name": item.R_Productname, "qnt": item.R_Product_Unit, "exp_date": item.R_ProductExp, "price": item.R_price, "nop": item.R_Product_Qut, "image": item.R_image, "cate_id": item.R_Category_id })
                    // { "name":item.R_Productname , "qnt": item.R_Product_Unit , "exp_date":item.R_ProductExp , "price":item.R_price, "nop":item.R_Product_Qut , "image":item.R_image, "cate_id":item.R_Category_id  }
                });

                val = await data_api.json()

                console.log("after  Add Product", val);

                data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Edit Product", "Edit_Product_id": item.R_id })
                });

                val = await data_api.json()
                console.log(val)
                alert("finally Add Product successfully", val)




            } else if (cat == "DeleteProduct") {
                data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                    method: "put", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Delete Delete_Product", "request_id": item.R_id, "status": true })
                });

                val = await data_api.json()
                alert("Request Approved", val)


                data_api = await fetch('http://127.0.0.1:5000/api/product', {
                    method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                    body: JSON.stringify({ "id": item.R_Product_id })
                    // { "name":item.R_Productname , "qnt": item.R_Product_Unit , "exp_date":item.R_ProductExp , "price":item.R_price, "nop":item.R_Product_Qut , "image":item.R_image, "cate_id":item.R_Category_id  }
                });

                val = await data_api.json()

                console.log("after  Add Product", val);

                data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Delet Delete_Product", "Delete_DeleteProduct_id": item.R_id })
                });

                val = await data_api.json()

                alert("finally Add Product successfully", val)



            } else if (cat == "DeleteCategory") {

                data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                    method: "put", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Delete Delete_Category", "request_id": item.R_id, "status": true })
                });

                val = await data_api.json()
                alert("Request Approved", val)

                data_api = await fetch('http://127.0.0.1:5000/api/category', {
                    method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                    body: JSON.stringify({ "id": item.R_Category_id })
                    // { "name":item.R_Productname , "qnt": item.R_Product_Unit , "exp_date":item.R_ProductExp , "price":item.R_price, "nop":item.R_Product_Qut , "image":item.R_image, "cate_id":item.R_Category_id  }
                });

                val = await data_api.json()

                console.log("after  Add Product", val);


                data_api = await fetch('http://127.0.0.1:5000/testimonial', {
                    method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    body: JSON.stringify({ "request": "Delete_DeleteProduct_id Delete_Category", "Delete_DeleteProduct_id": item.R_id })
                });

                val = await data_api.json()

                alert("finally Add Product successfully", val)





            }

        },
        async add_Cat_App() {

            Token = localStorage.getItem("token")
            data_api = await fetch('http://127.0.0.1:5000/admin/testimonial', {
                method: "get", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                body: JSON.stringify()
            });

            val = await data_api.json()
            console.log("All request",val)
            // console.log("Request testimonial ", val["AddCategory"], val["AddCategory"].length)


            for (i = 0; i <= val["AddCategory"].length - 1; i++) {
                if (val["AddCategory"][i]["R_approved"] == true) {
                    // // Add category 

                    // add category when request have approved

                    fetch('http://127.0.0.1:5000/api/category', {
                        method: "POST", headers: { 'content-type': 'application/json' },
                        body: JSON.stringify({ "name": val["AddCategory"][i]["R_Category_name"], "user_id": val["AddCategory"][i]["R_user_id"] })
                    })

                        .then(response => {
                            // Check if the response status is OK (status code 200)
                            if (!response.ok) {
                                throw new Error(`HTTP error! Status: ${response.status}`);
                            }
                            // Parse the JSON response (assuming it's JSON data)
                            return response.json();
                        })
                        .then(data => {
                            // Now 'data' contains the response data from the API

                            console.log("Add Cate", data);
                        })
                        .catch(error => {
                            console.error("Failed to fetch data from the API:", error);
                        });


                    // after add category delete request 

                    fetch('http://127.0.0.1:5000/api/testimonial', {
                        method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                        body: JSON.stringify({ "request": "Add Category", "Add_Category_id": val["AddCategory"][i]["R_id"] })
                    })

                        .then(response => {
                            // Check if the response status is OK (status code 200)
                            if (!response.ok) {
                                throw new Error(`HTTP error! Status: ${response.status}`);
                            }
                            // Parse the JSON response (assuming it's JSON data)
                            return response.json();
                        })
                        .then(data => {
                            // Now 'data' contains the response data from the API
                            console.log("Delet Add category request", data);
                        })
                        .catch(error => {
                            console.error("Failed to fetch data from the API:", error);
                        });



                } else {
                    //   console.log(val["AddCategory"][i]["R_approved"])
                    this.Add_Category.push(val["AddCategory"][i])

                }
            }


            // this loop for Edit Category


            for (i = 0; i <= val["EditCategory"].length - 1; i++) {
                if (val["EditCategory"][i]["R_approved"] == true) {



                    fetch('http://127.0.0.1:5000/api/category', {
                        method: "put", headers: { 'content-type': 'application/json' },
                        body: JSON.stringify({ "name": val["EditCategory"][i]["R_Category_name"], "id": val["EditCategory"][i]["R_Category_id"] })
                    })

                        .then(response => {
                            // Check if the response status is OK (status code 200)
                            if (!response.ok) {
                                throw new Error(`HTTP error! Status: ${response.status}`);
                            }
                            // Parse the JSON response (assuming it's JSON data)
                            return response.json();
                        })
                        .then(data => {
                            // Now 'data' contains the response data from the API

                            console.log("Edit Category", data);
                        })
                        .catch(error => {
                            console.error("Failed to fetch data from the API:", error);
                        });


                    fetch('http://127.0.0.1:5000/api/testimonial', {
                        method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                        body: JSON.stringify({ "request": "Edit Category", "Edit_Category_id": val["EditCategory"][i]["R_id"] })
                    })

                        .then(response => {
                            // Check if the response status is OK (status code 200)
                            if (!response.ok) {
                                throw new Error(`HTTP error! Status: ${response.status}`);
                            }
                            // Parse the JSON response (assuming it's JSON data)
                            return response.json();
                        })
                        .then(data => {
                            // Now 'data' contains the response data from the API
                            console.log("Delete Edit category request", data);
                        })
                        .catch(error => {
                            console.error("Failed to fetch data from the API:", error);
                        });






                } else if (val["EditCategory"][i]["R_approved"] == false) {
                    this.Edit_Category.push(val["EditCategory"][i])

                }
            }


            // console.log("Request from Add Product",val["AddProduct"])
            for (i = 0; i <= val["AddProduct"].length - 1; i++) {
                if (val["AddProduct"][i]["R_approved"] == true) {
                    console.log("From Add Product", val["AddProduct"][i])



                    // add Produc in Product table
                    fetch('http://127.0.0.1:5000/api/product', {
                        method: "POST", headers: { 'content-type': 'application/json' },
                        body: JSON.stringify({ "name": val["AddProduct"][i]["R_Productname"], "qnt": val["AddProduct"][i]["R_Product_Unit"], "exp_date": val["AddProduct"][i]["R_ProductExp"], "price": val["AddProduct"][i]["R_price"], "nop": val["AddProduct"][i]["R_Product_Qut"], "image": val["AddProduct"][i]["R_image"], "cate_id": val["AddProduct"][i]["R_Category_id"] })
                        // })
                    })

                        .then(response => {
                            // Check if the response status is OK (status code 200)
                            if (!response.ok) {
                                throw new Error(`HTTP error! Status: ${response.status}`);
                            }
                            // Parse the JSON response (assuming it's JSON data)
                            return response.json();
                        })
                        .then(data => {
                            // Now 'data' contains the response data from the API

                            console.log("Add Product", data);
                        })
                        .catch(error => {
                            console.error("Failed to fetch data from the API:", error);
                        });

                    fetch('http://127.0.0.1:5000/api/testimonial', {
                        method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },
                        body: JSON.stringify({ "request": "Add Product", "Add_Product_id": val["AddProduct"][i]["R_Product_id"] })
                    })

                        .then(response => {
                            // Check if the response status is OK (status code 200)
                            if (!response.ok) {
                                throw new Error(`HTTP error! Status: ${response.status}`);
                            }
                            // Parse the JSON response (assuming it's JSON data)
                            return response.json();
                        })
                        .then(data => {
                            // Now 'data' contains the response data from the API
                            console.log("Delete Add Product request", data);
                        })
                        .catch(error => {
                            console.error("Failed to fetch data from the API:", error);
                        });







                } else if (val["AddProduct"][i]["R_approved"] == false) {
                    // console.log("AddProduct not approved",val["AddProduct"][i])
                    this.Add_Product.push(val["AddProduct"][i])

                }

                //   this.Add_Product.push(val["AddProduct"][i])

            }
            console.log("this is final Add request", this.Add_Product)



            console.log("Request", val["EditProduct"].length - 1)
            for (i = 0; i <= val["EditProduct"].length - 1; i++) {
                if (val["EditProduct"][i]["R_approved"] == true) {
                    console.log(val["EditProduct"][i])

                } else if (val["EditProduct"][i]["R_approved"] == false) {
                    this.Edit_Product.push(val["EditProduct"][i])

                }



            }



            console.log("Delete Product Request", val)
            for (i = 0; i <= val["DeleteProduct"].length - 1; i++) {
                if (val["DeleteProduct"][i]["R_approved"] == true) {

                    // this.Delete_Product.push(val["DeleteProduct"][i])

                    // fetch('http://127.0.0.1:5000/api/product', {
                    //     method: "delete", headers: { 'content-type': 'application/json','Authorization': `Bearer ${Token}`  },
                    //     body: JSON.stringify({ "id":val["DeleteProduct"][i]["R_Product_id"]})
                    //                                 // { "name":item.R_Productname , "qnt": item.R_Product_Unit , "exp_date":item.R_ProductExp , "price":item.R_price, "nop":item.R_Product_Qut , "image":item.R_image, "cate_id":item.R_Category_id  }
                    //     })

                    //     .then(response => {
                    //         // Check if the response status is OK (status code 200)
                    //         if (!response.ok) {
                    //             throw new Error(`HTTP error! Status: ${response.status}`);
                    //         }
                    //         // Parse the JSON response (assuming it's JSON data)
                    //         return response.json();
                    //     })
                    //     .then(data => {
                    //         // Now 'data' contains the response data from the API

                    //         console.log("Add Product", data);
                    //     })
                    //     .catch(error => {
                    //         console.error("Failed to fetch data from the API:", error);
                    //     });


                    //     fetch('http://127.0.0.1:5000/testimonial', {
                    //     method: "delete", headers: { 'content-type': 'application/json', 'Authorization': `Bearer ${Token}` },

                    //     body: JSON.stringify({ "request": "Delet Delete_Product", "Delete_DeleteProduct_id":val["DeleteProduct"][i]["R_id"] })
                    // })

                    //         .then(response => {
                    //             // Check if the response status is OK (status code 200)
                    //             if (!response.ok) {
                    //                 throw new Error(`HTTP error! Status: ${response.status}`);
                    //             }
                    //             // Parse the JSON response (assuming it's JSON data)
                    //             return response.json();
                    //         })
                    //         .then(data => {
                    //             // Now 'data' contains the response data from the API
                    //             console.log("Delete Add Product request", data);
                    //         })
                    //         .catch(error => {
                    //             console.error("Failed to fetch data from the API:", error);
                    //         });



                } else {
                    this.Delete_Product.push(val["DeleteProduct"][i])

                }

            }

            console.log("Delete Category Request", val["DeleteCategory"].length - 1)
            for (i = 0; i <= val["DeleteCategory"].length - 1; i++) {
                if (val["DeleteCategory"][i]["R_approved"] == true) {
                    console.log(val["DeleteCategory"][i])
                    // this.Delete_Category.push(val["DeleteCategory"][i])



                } else {
                    this.Delete_Category.push(val["DeleteCategory"][i])
                }

            }


        }
    },
})