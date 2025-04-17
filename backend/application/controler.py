from application.models import db
from flask import current_app as app
from flask import render_template,request,jsonify,make_response,session
from application.models import User,Category,Product,requestProduct,requestCategory,ShoppingCart,CartItem

from flask_restful import Resource,Api,fields,marshal_with,request,reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import datetime 
# from api import role_required

from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
import jwt
import json
import requests

# from application.tasks import ManegerReport_csv
# from flask import send_from_directory
# from flask import send_file
# import os






@app.route('/userragister',methods=["GET","POST"])
def userragister():
  data = request.get_json()
  if data.get("emailid") and data.get("Username") and data.get("Password") and data.get("Role"):
    user=User.query.filter_by(emailid=data.get("emailid") ).first()
    if not user:
        ragister_user=User(emailid=data.get("emailid"),Username=data["Username"],Password=generate_password_hash(data.get("Password")) ,Role=data.get("Role"),active=False)
        db.session.add(ragister_user)
        db.session.commit()
        return {"message":"Ragister successfully"},201
    else:
                return {"message":"User already have try diffrent"},401
  else:
        return {"message":"Missing vaule"},400


@app.route('/userlogin',methods=["POST"])
def userLogin():
        
        data = request.get_json()
        if data.get("emailid") and data.get("Password") :
            user=User.query.filter_by(emailid=data.get("emailid") ).first()

            print(user.Role,data.get("type"),check_password_hash(user.Password, data['Password']))
            if  user.Role==data.get("type") and check_password_hash(user.Password, data['Password']):
                    
                    access_token=create_access_token(identity={"Email_id":user.emailid,"Username":user.Username,"Role":user.Role},expires_delta=datetime.timedelta(hours=1))
                    current_time = datetime.datetime.now()
                    user.datetime=current_time
                    db.session.add(user)
                    db.session.commit()

                    return {"message":"Login successfully","Username":user.Username,"Email_id":user.emailid,"Roll":user.Role,"token":access_token},201
            else:
                return {'message': 'Invalid email or password'}, 401
            # return "Login"
            
        else:
                return {"message":"Missing vaule"},400


all_cates = {
    'Category_id': fields.Integer,
    'Categoryname':fields.String,
    'User_id':fields.Integer,
    'Date':fields.DateTime
}

@app.route('/category/<user>',methods=["GET","POST","PUT","DELETE"])
@marshal_with(all_cates)
@jwt_required()
def category(user):
    current_user = get_jwt_identity()
    print("Problem is here ","user",current_user)
    
    if request.method=="GET":
        user_id=User.query.filter_by(emailid=current_user["Email_id"]).first()
        if user=="manager":
            cates = Category.query.filter_by(User_id=user_id.User_id).all() 
            print("category Faizan ALi Manager",cates,current_user)
        
        else:
            cates = Category.query.all()
        return cates
    
    elif request.method=="POST":

        data = request.get_json()
        if data:
            cates = Category.query.filter_by(Categoryname = data.get("Categoryname")).first()

            if cates == None  :
                    current_time = datetime.datetime.now()
                    new_category = Category(Categoryname=data.get("Categoryname"),User_id=data.get("User_id"),datatime=current_time)
                    db.session.add(new_category)
                    db.session.commit()
                    return {'massage':'Category add successfully'}

            error = f"{data.get("Categoryname")}, is already exist!"
            return {'massage':error}
        else:
            return {'massage':'Please fill out the category! name and user_id'}     
        
    elif request.method=="PUT":
        data = request.get_json()

        if data and data.get("Category_id") and  data.get("Categoryname"):
            cate = Category.query.get(data.get("Category_id"))
            cate.Categoryname = data.get("Categoryname")
            db.session.commit()
            return {'massage':'Category update successfully'}
        else:
            return {'massage':'Please, fill out category name! for change name '}
        
    elif request.method=="DELETE":

        data = request.get_json()
        category = Category.query.filter_by(Categoryname=data.get("Categoryname")).first()
        print("Category name ",category)
        if category:

            prods = Product.query.filter_by(Category_id=category.Category_id).all()
            if prods:
                for prod in prods:
                    db.session.delete(prod)
                    db.session.commit()
            db.session.delete(category)
            db.session.commit()  
            return {'massage':'Category deleted successfully'}
        else:
            return {'massage':'Category does not  Exist'}

all_prods = {
    
    'Product_id':fields.Integer,
    'Productname':fields.String,
    'Unit':fields.String,
    'Exp':fields.String,
    'MFG':fields.String,

    'image':fields.String,
    'price':fields.Float,
    'Qut':fields.Integer,
    'Category_id':fields.Integer
}

@app.route('/Products',methods=["GET","POST","PUT","DELETE"])
@marshal_with(all_prods)
def Products():
        if request.method == "GET":
            prods = Product.query.all()
            return prods

        elif request.method == "POST":
       
            data = request.get_json()
            if data.get("Productname") and data.get("Qut") and data.get("Unit") and data.get("price") and data.get("MFG") and data.get("Exp") and data.get("image") and data.get("Category_id"):

                    new_prod = Product( Productname=data.get("Productname"),
                                        Qut=data.get("Qut"),
                                        Unit=data.get("Unit"),                                        
                                        price=data.get("price"),
                                        MFG=data.get("MFG"),
                                        Exp=data.get("Exp"),
                                        image=data.get("image"),
                                        datetime=datetime.datetime.now(),
                                        Category_id=data.get("Category_id")
                                        )
                    
                    db.session.add(new_prod)
                    db.session.commit()
                    return {'massage':'Product add successfully'}
            else:

                return {'massage':'Provide all Details of Product','Detail':'name and qnt and exp_date and price and nop cate_id and image'}

        elif request.method=="PUT":

            data = request.get_json()
            if data.get("Product_id"):
                prod = Product.query.filter_by(Product_id=data.get("Product_id")).first()
                if data.get("Productname") != None:
                     prod.Productname = data.get("Productname")
                if data.get("Qut") != None:
                     prod.Qut = data.get("Qut") 
                if data.get("Unit") !=None:
                     prod.Unit = data.get("Unit")
                if data.get("price") != None:
                     prod.MFG = data.get("MFG")
                if data.get("MFG") != None :
                     prod.Exp = data.get("Exp")
                if data.get("Exp") != None :
                     prod.price = data.get("price")
                if data.get("image") != None:  
                    prod.image = data.get("image")   
                if data.get("Category_id") != None:
                     prod.Category_id = data.get("Category_id")   

                db.session.commit()
                return {'massage':'Product update successfully'},200
            else:
                return {'massage':'Please provide prod_id first and then value for change'},404

        elif request.method=="DELETE":
            data=request.get_json("Product_id")
            prod = Product.query.get(data.get("Product_id"))
            if prod:
                db.session.delete(prod)
                db.session.commit()
                return {'massage':'Product deleted successfully'}
            else:
                return {'massage':'Product Not found'}
             

#   "Productname":"Milk Cacke",
#   "Qut":10,
#   "Unit":"pr/pease",                                
#   "price":50,
#   "MFG":"10/12/2030",
#   "Exp":"10/12/2031",
#   "image":"/sdsfsdfsdfsd",
#   "Category_id":1
@app.errorhandler(401)
def unauthorised(error):
    return 'unauthorised user', 401


@app.route('/requestProduct',methods=["GET","POST","DELETE","PUT"])
@jwt_required()
def request_Product():
    
    if request.method =="GET":
        try :
            current_user = get_jwt_identity()
           
            email_id = current_user.get('Email_id')

            if current_user.get('Role')=='ADMIN':

                req_Product=requestProduct.query.all()
                for req in req_Product:
                    
                        if req.R_P_type=="POST" :
                            check_prod= Product.query.filter_by(Productname=req.R_P_name,price=req.R_price).first()
                            if check_prod is None:
                         
                         
                                new_prod = Product( Productname=req.R_P_name,
                                                    Qut=req.R_Qut,
                                                    Unit=req.R_Unit,                                        
                                                    price=req.R_price,
                                                    MFG=req.R_MFG,
                                                    Exp=req.R_Exp,
                                                    image=req.R_image,
                                                    datetime=datetime.datetime.now(),
                                                    Category_id=req.R_C_id
                                                    ) 
                                db.session.add(new_prod)
                                db.session.commit()
                                print("not already exisit prods")
                            else:
                                print("message : Product is already in inventory")
                                 
                        elif req.R_P_type=="DELETE":
                            check_prod= Product.query.filter_by(Productname=req.R_P_name,price=req.R_price).first()
                            if check_prod is not None:
                                 db.session.delete(check_prod)
                                 db.session.commit()
                            else:
                                print("message : Product Not found")
                            
                        elif req.R_P_type=="PUT":
                            check_prod= Product.query.filter_by(Productname=req.R_P_name,price=req.R_price).first()
                            if check_prod is not None:
                                response =  requests.put('/Products',data=req)
                                if response:
                                    print(response)
                            else:
                                print("message : Product Not found")   
                                 
                 
            elif current_user.get('Role')=='maneger':
                user_= User.query.filter_by(emailid=email_id).first()
                req_Product = requestProduct.query.filter_by(R_user_id = user_.User_id).all()
            Dist_requestProduct = []
            print("req_prods",req_Product)
            
            if len(req_Product) !=0:
                for i in range(len(req_Product)):
                    Dist_requestProduct.append({"R_id":0,
                                                "R_C_id":0,
                                                "R_P_id":"",
                                                "R_P_name":"",
                                                "R_Unit":0,
                                                "R_Qut":0,
                                                "R_price":"",
                                                "R_MFG":"",
                                                "R_Exp":"",
                                                "R_image":"",
                                                "R_approved":False,
                                                "R_P_type":"",
                                                "datetime":""})
                    
                print(req_Product[0].R_id,"len",len(Dist_requestProduct))
                for i in range(len(req_Product)):
                        Dist_requestProduct[i]["R_id"]=req_Product[i].R_id
                        Dist_requestProduct[i]["R_C_id"]=req_Product[i].R_C_id
                        Dist_requestProduct[i]["R_P_id"]=req_Product[i].R_P_id
                        Dist_requestProduct[i]["R_P_name"]=req_Product[i].R_P_name
                        Dist_requestProduct[i]["R_Unit"]=req_Product[i].R_Unit
                        Dist_requestProduct[i]["R_Qut"]=req_Product[i].R_Qut
                        Dist_requestProduct[i]["R_price"]=req_Product[i].R_price
                        Dist_requestProduct[i]["R_MFG"]=req_Product[i].R_MFG
                        Dist_requestProduct[i]["R_Exp"]=req_Product[i].R_Exp
                        Dist_requestProduct[i]["R_image"]=req_Product[i].R_image
                        Dist_requestProduct[i]["R_approved"]=req_Product[i].R_approved
                        Dist_requestProduct[i]["R_P_type"]=req_Product[i].R_P_type
                        Dist_requestProduct[i]["datetime"]=req_Product[i].datetime
                        print(req_Product[i],"Faizan you are close to success ")
            return Dist_requestProduct , 200
        except Exception as e :
            print(e)
            return {'message' : "Internal Server Error"}, 500
# {

#   "R_C_id":1,
#   "R_P_name":"Cake",
#   "R_Unit":"kg/pr",
#   "R_Qut":10,
#   "R_price":50,
#   "R_MFG":"20/06/2024",
#   "R_Exp":"20/07/2025",
#   "R_P_type":"POST"

# }
    elif request.method =="POST":
      
            current_user = get_jwt_identity()
            data = request.get_json()
            user_email = current_user.get('Email_id')
            user_=User.query.filter_by(emailid = user_email).first()
            print("User_id",user_.User_id,data.get('R_C_id'))
            if  user_ :
                if data.get('R_C_id') and data.get('R_P_name') and data.get('R_Unit') and  data.get('R_Qut') and  data.get('R_price') and data.get('R_MFG') and data.get('R_Exp') and data.get('R_image') and  data.get('R_P_type'):
                    new_prod = requestProduct( 
                                            R_C_id = data.get('R_C_id'),
                                            R_P_id = "None",
                                            R_P_name = data.get('R_P_name'),
                                            R_Unit = data.get('R_Unit'),
                                            R_Qut = data.get('R_Qut'),
                                            R_price = data.get('R_price'),
                                            R_MFG = data.get('R_MFG'),
                                            R_Exp = data.get('R_Exp'),
                                            R_image = data.get('R_image'),
                                            R_approved = False,
                                            R_P_type = data.get('R_P_type'),
                                            datetime = datetime.datetime.now(),
                                            R_user_id = user_.User_id,
                                            ) 
                    db.session.add(new_prod)
                    db.session.commit()
                    return {'massage':'Request Product add successfully'},200
                    
                else:
                    return {'massage':'Provide all Details of Product','Detail':'name and qnt and exp_date and price and nop cate_id and image'},400
    elif request.method =="PUT":
                current_user = get_jwt_identity()
                data = request.get_json()
                if current_user.get("Role")=="ADMIN":
                    req =requestProduct.query.filter_by(R_id=data["R_id"]).first()
                    req.R_approved=True
                    db.session.commit()
                    print(data["R_id"])
                    return {"message":"Approved product request"}
            
                return {'massage':'User Athontication'},401


    elif request.method == "DELETE":
            current_user = get_jwt_identity()
            data = request.get_json()
            user_email = current_user.get('Email_id')
            user_=User.query.filter_by(emailid = user_email).first()
            if user_:
                if data.get('R_id'):
                    r_product = requestProduct.query.get(int(data.get('R_id')))
                    db.session.delete(r_product)
                    db.session.commit()
                    return {'massage':'Delete Successfully'}
                else:
                    print(r_product,data.get('R_id'))
                    return {'massage':'Provide R_product_id Product'},400
                  
            else:
                    return {'massage':'User Athontication'},401
                 

@app.route('/categoryProduct',methods=["GET","POST","DELETE","PUT"])
@jwt_required()
def category_Product():
    if request.method == "GET":
        current_user = get_jwt_identity()
        request_Category = []
        email_id = current_user.get('Email_id')
        if current_user.get('Role')=='ADMIN':
                
                request_Category=requestCategory.query.all()

                for req in request_Category:
                    

                    check_category = Category.query.filter_by(Categoryname=req.R_C_name).all()
                    

                    if req.R_C_type=="POST" and req.R_approved==1 and check_category ==[] :
                        new_category=Category(Categoryname=req.R_C_name,User_id=req.R_user_id)
                        db.session.add(new_category)
                        db.session.commit()
                       
                    elif req.R_C_type=="DELETE" and req.R_approved==1 and len(check_category) != 0 :
                     
                        cate=Category.query.filter_by(Categoryname=req.R_C_name).first()
                        db.session.delete(cate)
                        db.session.commit()
                       
                    
                    elif req.R_C_type=="PUT" and req.R_approved==1 and  check_category is not None:
                        # url = f"http://localhost:5173/category/{current_user.get('Role')}"
                        # response=requests.put(url=url,data=req)
                        # if response:
                        #       print("{'massage':'Delete Successfully'}")
                        # else:
                             print("error for PUT Request",req)
                         
                         
        
                
                 
        elif current_user.get('Role')=='maneger':
                # user_= User.query.filter_by(emailid=email_id).first()
                # request_Category = requestCategory.query.filter_by(R_user_id = user_.User_id).all()
                print("This is the  problem ")
        Dict_=[]
        if len(request_Category)!=0:
                for i in range(len(request_Category)):
                    request_category = {
                            "R_id":0,
                            "R_C_name":"",
                            "R_C_type":"",
                            "R_approved":"",
                            "R_user_id":"",
                            "datetime":""
                            } 
                    Dict_.append(request_category)  
                for i in range(len(request_Category)):
                         
                    Dict_[i]["R_id"]=request_Category[i].R_id
                    Dict_[i]["R_C_name"]=request_Category[i].R_C_name
                    Dict_[i]["R_C_type"]=request_Category[i].R_C_type
                    Dict_[i]["R_approved"]=request_Category[i].R_approved
                    Dict_[i]["R_user_id"]=request_Category[i].R_user_id
                    Dict_[i]["datetime"]=request_Category[i].datetime
             
                return Dict_
                
        else:
                return Dict_

    elif request.method=="POST":
        current_user = get_jwt_identity()
        data = request.get_json()
        user_email = current_user.get('Email_id')
        user_=User.query.filter_by(emailid = user_email).first()
        if user_ :
            if data.get("R_C_name") and data.get("R_C_type") :
                check_cats=Category.query.filter_by(Categoryname=data.get("R_C_name")).first()
               
                if check_cats :
                    if data.get("R_C_type") ==  "POST":
                        return {"message":"Category Already in database"},400
                    
                
                request_addCatregory=requestCategory(

                        R_C_name=data.get("R_C_name"),
                        R_C_type=data.get("R_C_type"),
                        R_approved=False,
                        datetime=datetime.datetime.now(),
                        R_user_id=user_.User_id,
                        
                    )
                db.session.add(request_addCatregory)
                db.session.commit()
                return jsonify({"message":"Successfully Added"}),200
            else:
                return {"message":"Provide Details"},400
        else:
                return {'massage':'User Athontication'},401

    elif request.method =="PUT":
                
                current_user = get_jwt_identity()
                data = request.get_json()
              
                if current_user.get("Role")=="ADMIN":
                    req =requestCategory.query.filter_by(R_id=data["R_id"]).first()
                    req.R_approved=True
                    db.session.commit()
                    print(req)
                    print(data["R_id"])
                    return {"message":"Approved Category request"}
                # print(data,"Faizan")
                return {'massage':'User Athontication'},401

    elif request.method == "DELETE":
            current_user = get_jwt_identity()
            data = request.get_json()
            user_email = current_user.get('Email_id')
            user_=User.query.filter_by(emailid = user_email).first()
            if user_:
                if data.get('R_id'):
                    r_category = requestCategory.query.get(int(data.get('R_id')))
                    db.session.delete(r_category)
                    db.session.commit()
                    return {'massage':'Delete Successfully'}
                else:
                    print(r_category,data.get('R_id'))
                    return {'massage':'Provide R_category_id Product'},400
                  
            else:
                    return {'massage':'User Athontication'},401
@app.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    data = request.get_json()
    current_user = get_jwt_identity()
    email_id = current_user.get('Email_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    user = User.query.filter_by(emailid =email_id).first()
    product = Product.query.get(product_id)
    
    if not user or not product:
        return jsonify({"error" : "Invalid user or product"}), 404

    cart = ShoppingCart.query.filter_by(user_id=user.User_id).first()

    if not cart:
        cart = ShoppingCart(user_id=user.User_id,created_at=datetime.datetime.now())
        db.session.add(cart)

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product.Product_id).first()

    if cart_item:
        cart_item.quantity += quantity  # Update quantity if already in cart
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product.Product_id, quantity=quantity,added_at=datetime.datetime.now())
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({"message": "Product added to cart"}), 201


@app.route('/cart/<int:cart_item_id>', methods=['PUT'])
def update_cart_item(cart_item_id):


    cart_item = CartItem.query.get(cart_item_id)

    if cart_item:
        if cart_item.quantity >1: 
            cart_item.quantity -= 1
        else:
             db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Cart item updated successfully"}), 200
    else:
        return jsonify({"error": "Cart item not found"}), 404
    
@app.route('/cart', methods=['GET'])
@jwt_required()
def get_cart_items():
    current_user = get_jwt_identity()
    user=User.query.filter_by(emailid=current_user.get("Email_id")).first()
    cart = ShoppingCart.query.filter_by(user_id=user.User_id).first()

    if not cart:
        return jsonify({"message": "No shopping cart found"}), 404

    cart_items = CartItem.query.filter_by(cart_id=cart.id).all()

    items = []
    for item in cart_items:
        items.append({
            'cart_item_id': item.id,
            'product_id': item.product_id,
            'product_name': item.product.Productname,
            'product_image': item.product.image,
            'price': item.product.price,
            'quantity': item.quantity,
            'total_price': item.total_price
        })

    return jsonify({'cart_items': items}), 200

@app.route('/cart/<int:cart_item_id>', methods=['DELETE'])
def delete_cart_item(cart_item_id):
    cart_item = CartItem.query.get(cart_item_id)

    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Cart item deleted successfully"}), 200
    else:
        return jsonify({"error": "Cart item not found"}), 404
