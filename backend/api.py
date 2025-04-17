from flask_restful import Resource,Api,fields,marshal_with,request,reqparse
from application.models import User,Category,Product,BuyProduct,Cart,db,AddCategory,EditCategory,AddProduct,EditProduct,DeleteProduct,DeleteCategory
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask import Flask, make_response
import json
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required
from functools import wraps
import jwt
import datetime
 
# using now() to get current time




api = Api(app)
 
all_cates = {
    'Category_id': fields.Integer,
    'Categoryname':fields.String,
    'buy_id':fields.Integer
}
all_prods = {
    
    'Product_id':fields.Integer,
    'Productname':fields.String,
    'Product_Unit':fields.String,
    'image':fields.String,
    'ProductExp':fields.String,
    'price':fields.String,
    'Product_Qut':fields.Integer,
    'Category_id':fields.Integer
}

all_cart = {
    'id':fields.Integer,
    'prod_id': fields.Integer,
    'nop':fields.Integer,
    'user_id':fields.Integer


}


cate_parser = reqparse.RequestParser()
cate_parser.add_argument('user_id')
cate_parser.add_argument('id')
cate_parser.add_argument('name')


prod_parser = reqparse.RequestParser()
prod_parser.add_argument('id')
prod_parser.add_argument('name')
prod_parser.add_argument('qnt')
prod_parser.add_argument('mfg_date')
prod_parser.add_argument('exp_date')
prod_parser.add_argument('price')
prod_parser.add_argument('nop')
prod_parser.add_argument('image')
prod_parser.add_argument('cate_id')


card_parser = reqparse.RequestParser()
card_parser.add_argument('user_id')
card_parser.add_argument('id')
card_parser.add_argument('nop')
# card_parser.add_argument('name')


    



#User Ragistration Api
class UserRagistration(Resource):
    def post(self):
        data = request.get_json()
        if data.get("Username") and data.get("Password") and data.get("Role"):
            user=User.query.filter_by(Username=data.get("Username") ).first()
            if not user:
                ragister_user=User(Username=data["Username"],Password=generate_password_hash(data.get("Password")) ,Role=data.get("Role"),active=False)
                db.session.add(ragister_user)
                db.session.commit()
                return {"message":"Ragister successfully"},201
            else:
                return {"message":"User already have try diffrent"},401
        else:
                return {"message":"Missing vaule"},400



def set_authorization_header(token):
        # Create a response object
        response = make_response('Response with Authorization Header')

        # Set the 'Authorization' header with a token or credentials
        response.headers['Authorization'] = 'Bearer {{token}}'

        # Optionally, set other headers as needed
        # response.headers['Content-Type'] = 'application/json'

        return response


 
#User Login Api
class UserLogin(Resource):
   

    def post(self):
        
        data = request.get_json()
        print(data)
        if data.get("Username") and data.get("Password") :
            user=User.query.filter_by(Username=data.get("Username") ).first()
            if  user and check_password_hash(user.Password, data['Password']):
                
                
                access_token=create_access_token(identity={"User_id":user.User_id,"Username":user.Username,"Role":user.Role})
                current_time = datetime.datetime.now()
                print("Before Success",current_time,user.datetime)
                
                user.datetime=current_time
                db.session.add(user)
                db.session.commit()
                print("Success",current_time,user.datetime)

                return {"message":"Login successfully","Username":user.Username, "token":access_token},201
            else:
                return {'message': 'Invalid email or password'}, 401
        else:
                return {"message":"Missing vaule"},400



class TestimonialUserApi(Resource):
    '''
    API for testimonials of a general user
    ''' 
    @jwt_required()
    def get(self):
        try :
           
            current_user = get_jwt_identity()
            user_id = current_user.get('User_id')

            Add_Category = AddCategory.query.filter_by(R_user_id = user_id).all()
            # Add_Category = AddCategory.query.filter_by(R_approved = False).all()

            Dist_Add_Category = []
            if len(Add_Category) !=0:
                for i in range(len(Add_Category)):
                    Dist_Add_Category.append({"R_id":0,"R_Category_name":'',"R_approved":False,"R_user_id":0})

                for i in range(len(Dist_Add_Category)):
                        Dist_Add_Category[i]["R_id"]=Add_Category[i-1].R_id
                        Dist_Add_Category[i]["R_Category_name"]=Add_Category[i-1].R_Category_name
                        Dist_Add_Category[i]["R_approved"]=Add_Category[i-1].R_approved

                        Dist_Add_Category[i]["R_user_id"]=Add_Category[i-1].R_user_id

           
            

            Edit_Category = EditCategory.query.filter_by(R_user_id = user_id).all()
            Dist_Edit_Category = []
            
            if len(Edit_Category) !=0:

                for i in range(len(Edit_Category)):
                    Dist_Edit_Category.append({"R_id":0,"R_Category_name":'',"R_Category_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Edit_Category)):
                        Dist_Edit_Category[i]["R_id"]=Edit_Category[i-1].R_id
                        Dist_Edit_Category[i]["R_Category_name"]=Edit_Category[i-1].R_Category_name
                        Dist_Edit_Category[i]["R_Category_id"]=Edit_Category[i-1].R_Category_id
                        Dist_Edit_Category[i]["R_approved"]=Edit_Category[i-1].R_approved

                        Dist_Edit_Category[i]["R_user_id"]=Edit_Category[i-1].R_user_id

            Add_Product = AddProduct.query.filter_by(R_user_id = user_id).all()
            Dist_Add_Product = []
            
            if len(Add_Product) !=0:

            
                for i in range(len(Add_Product)):
                    Dist_Add_Product.append({"R_Product_id":0,"R_Category_id":0,"R_Productname":'',"R_Product_Unit":'',
                                        "R_Product_Qut":0,"R_price":0,"R_ProductExp":'',"R_image":'',"R_approved":False,"R_user_id":0})
                for i in range(len(Add_Product)):
                        Dist_Add_Product[i]["R_Product_id"]=Add_Product[i-1].R_Product_id
                        Dist_Add_Product[i]["R_Category_id"]=Add_Product[i-1].R_Category_id
                        Dist_Add_Product[i]["R_Productname"]=Add_Product[i-1].R_Productname
                        Dist_Add_Product[i]["R_Product_Unit"]=Add_Product[i-1].R_Product_Unit
                        Dist_Add_Product[i]["R_Product_Qut"]=Add_Product[i-1].R_Product_Qut
                        Dist_Add_Product[i]["R_price"]=Add_Product[i-1].R_price
                        Dist_Add_Product[i]["R_approved"]=Add_Product[i-1].R_approved
                        Dist_Add_Product[i]["R_image"]=Add_Product[i-1].R_image
                        Dist_Add_Product[i]["R_ProductExp"]=Add_Product[i-1].R_ProductExp
                        Dist_Add_Product[i]["R_user_id"]=Add_Product[i-1].R_user_id

          
            print(Dist_Add_Product)
            Edit_Product = EditProduct.query.filter_by(R_user_id = user_id).all()
            Dist_Edit_Product = []
          
            if len(Edit_Product) !=0:

                
                for i in range(len(Edit_Product)):
                    Dist_Edit_Product.append({"R_id":0,"R_Category_id":0,"R_Productname":'',"R_Product_Unit":'',
                                        "R_Product_Qut":0,"R_price":0,"R_ProductExp":'',"R_Product_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Add_Product)):
                        Dist_Edit_Product[i]["R_Product_id"]=Edit_Product[i-1].R_Product_id
                        Dist_Edit_Product[i]["R_Category_id"]=Edit_Product[i-1].R_Category_id
                        Dist_Edit_Product[i]["R_Productname"]=Edit_Product[i-1].R_Productname
                        Dist_Edit_Product[i]["R_Product_Unit"]=Edit_Product[i-1].R_Product_Unit
                        Dist_Edit_Product[i]["R_Product_Qut"]=Edit_Product[i-1].R_Product_Qut
                        Dist_Edit_Product[i]["R_price"]=Edit_Product[i-1].R_price
                        Dist_Edit_Product[i]["R_ProductExp"]=Edit_Product[i-1].R_ProductExp
                        Dist_Edit_Product[i]["R_Product_id"]=Edit_Product[i-1].R_Product_id
                        Dist_Edit_Product[i]["R_approved"]=Edit_Product[i-1].R_approved

                        Dist_Edit_Product[i]["R_user_id"]=Edit_Product[i-1].R_user_id


            Delete_Product = DeleteProduct.query.filter_by(R_user_id = user_id).all()
            print("Delete_Product",Delete_Product)
            Dist_Delete_Product = []
          
            if len(Delete_Product) !=0:

                
                for i in range(len(Delete_Product)):
                    Dist_Delete_Product.append({"R_id":0,"R_Product_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Delete_Product)):
                        Dist_Delete_Product[i]["R_id"]=Delete_Product[i-1].R_id
                        Dist_Delete_Product[i]["R_Product_id"]=Delete_Product[i-1].R_Product_id
                        Dist_Delete_Product[i]["R_approved"]=Delete_Product[i-1].R_approved
                        Dist_Delete_Product[i]["R_user_id"]=Delete_Product[i-1].R_user_id  

            Delete_Category = DeleteCategory.query.filter_by(R_user_id = user_id).all()
            print("Delete_Category",Delete_Category)
            Dist_Delete_Category = []
          
            if len(Delete_Category) !=0:

                
                for i in range(len(Delete_Category)):
                    Dist_Delete_Category.append({"R_id":0,"R_Product_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Delete_Product)):
                        Dist_Delete_Category[i]["R_id"]=Delete_Category[i-1].R_id
                        Dist_Delete_Category[i]["R_Category_id"]=Delete_Category[i-1].R_Category_id
                        Dist_Delete_Category[i]["R_approved"]=Delete_Category[i-1].R_approved
                        Dist_Delete_Category[i]["R_user_id"]=Delete_Category[i-1].R_user_id            



            result = {
                'AddCategory' : Dist_Add_Category,
                'EditCategory' : Dist_Edit_Category,
                'AddProduct':Dist_Add_Product,
                'EditProduct' : Dist_Edit_Product,
                'DeleteProduct':Dist_Delete_Product,
                'DeleteCategory':Dist_Delete_Category
                
            } 
            print(result)
            return result , 200
        except Exception as e :
            print(e)
            return {'message' : "Internal Server Error"} , 500
    
    @jwt_required()
    def post(self):
        try:
            current_user = get_jwt_identity()
            data = request.get_json()

            request_user = data.get('request')
            user_id = current_user.get('User_id')

            if request_user =="Add Product" :

                name = data.get('name')
                qnt = data.get('qnt')
            
                exp_date = data.get('exp_date')
                price = data.get('price')
                nop = data.get('nop')
                cate_id = data.get('cate_id')
                image = data.get('image')

                if name and qnt and exp_date and price and nop and cate_id and image :
                    check=Product.query.filter_by(Productname=name).first()
                    if  check == None:   
                        
                        new_prod = AddProduct(R_Productname=name,
                                            R_Product_Unit=qnt,
                                            
                                            R_ProductExp=exp_date,
                                            R_price=price,
                                            R_Product_Qut=nop,
                                            R_image=image,
                                            R_Category_id=cate_id,
                                            R_user_id=user_id
                                            )
                        
                        db.session.add(new_prod)
                        db.session.commit()
                        return {'massage':'Request Product add successfully'},200
                    else:
                     return {"message":"Product All Ready Have"} 
                else:

                    return {'massage':'Provide all Details of Product','Detail':'name and qnt and exp_date and price and nop cate_id and image'},401

                
            elif  request_user =="Add Category" :

                data = request.get_json()
                
                Categoryname = data.get('R_Category_name')
                
                if Categoryname :
                        cates = Category.query.filter_by( Categoryname = Categoryname ).first()
                        print("Able",Categoryname,cates)

                    
                        print(cates)
                        if cates == None  :
                            new_cate = AddCategory(R_Category_name=Categoryname,R_user_id=user_id)
                            db.session.add(new_cate)
                            db.session.commit()
                            return {'massage':'Request Category add successfully'}

                        error = f"{cate_name}, is already exist!"
                        return {'massage':error}
                        
            
                else:
                    
                    return {'massage':'Please fill out the Categoryname! name and user_id'}
                
            elif   request_user =="Edit Category":

                
                cate_id = data.get('Category_id')
                cate_name = data.get('Category_name')
                if cate_name and cate_id:
                    check_cate=Category.query.filter_by(Category_id=cate_id)
                    if check_cate:
                        print("id check",cate_id)
                        cate = EditCategory(R_Category_name=cate_name,R_Category_id=cate_id,R_user_id=user_id)
                        db.session.add(cate)
                        db.session.commit()
                        return {'massage':'Request Category update successfully'}
                    else:
                        return {'massage':' Category Not Found'}
                else:
                    return {'massage':'Please, fill out category name! for change name '}
                
            elif   request_user =="Edit Product":
                args = prod_parser.parse_args()
                prod_id = data.get('Product_id')
                name = args['name']
                qnt = args['qnt']
                mfg_date = args['mfg_date']
                exp_date = args['exp_date']
                price = args['price']
                nop = args['nop']
                image = args['image']
                cate_id = args['cate_id']
                
                if prod_id:
                    prod = Product.query.get(prod_id)
                    print("upadet",prod)
                    if prod:
                        if name !='':
                            edit_prod=EditProduct(R_Productname=name,R_Product_id =prod_id,R_user_id=user_id,R_Category_id=cate_id)
                            
                            # prod.Productname = name
                            
                        if qnt !="":
                            edit_prod=EditProduct(R_Product_Unit=qnt,R_Product_id =prod_id,R_user_id=user_id,R_Category_id=cate_id)

                        if exp_date !='':
                            edit_prod=EditProduct(R_ProductExp=exp_date,R_Product_id =prod_id,R_user_id=user_id,R_Category_id=cate_id)
                            
                        if   price !='' and price != None :
                            print(type(price))
                            edit_prod=EditProduct(R_price=price,R_Product_id =prod_id,R_user_id=user_id,R_Category_id=cate_id)

                            
                        if   nop != None :
                            print("nop",type(nop))
                            edit_prod=EditProduct(R_Product_Qut=nop,R_Product_id =prod_id,R_user_id=user_id,R_Category_id=cate_id)
                        
                        if   image !=''  :   
                            edit_prod=EditProduct(R_image=image,R_Product_id =prod_id,R_user_id=user_id,R_Category_id=cate_id)
                            prod.image = image
                        # if   cate_id != None  :
                        #     print("cate",type(cate_id))
                        #     edit_prod=EditProduct(R_Product_Qut=nop,R_user_id=user_id,R_Category_id=cate_id)
                        #     prod.Category_id = cate_id
                        db.session.add(edit_prod)
                        db.session.commit()
                        return {'massage':'Request Product update successfully'}
            elif   request_user =="Delete Product":
                        Product_id=data.get("Product_id")
                        check_product=Product.query.filter_by(Product_id=Product_id).first()
                        if check_product:
                           R_pro = DeleteProduct(R_Product_id=Product_id,R_user_id=user_id)
                           db.session.add(R_pro)
                           db.session.commit()
                           return {"message":"Request Successfully Sent For delet Product "}
                        else:
                             return {"message":"Product Not Found"}
                             


            elif   request_user =="Delete Category":     
                        Category_id=data.get("Category_id")
                        check_category=Category.query.filter_by(Category_id=Category_id).first()
                        if check_category:
                           R_pro = DeleteCategory(R_Category_id=Category_id,R_user_id=user_id)
                           db.session.add(R_pro)
                           db.session.commit()
                           return {"message":"Request Successfully Sent For Delete Category "}
                        else:
                             return {"message":"Category Not Found"}
                             
                         
                # else:
                #     return {'massage':'Please provide Product_id first and then value for change'}

                 
            else:
                return {'message': 'Missing details'}, 400

            

        except Exception as e:
            print(e)
            return {'message' : "Internal Server Error"} , 500
    @jwt_required()
    def delete(self):
        try:
            current_user = get_jwt_identity()
            data = request.get_json()
            print(data["request"])
            if data["request"]=="Add Product":
                 delet_Add_Product_id=data.get("Add_Product_id")
                 R_detele = AddProduct.query.filter_by(R_Product_id=delet_Add_Product_id).first()
                 if R_detele == None:
                      return {"message":"Request Not Fount"}
                 else:
                      db.session.delete(R_detele)
                      db.session.commit()
                      
            elif data["request"]=="Edit Product":
                delet_Add_Product_id=data.get("Edit_Product_id")
                R_detele = EditProduct.query.filter_by(R_id=delet_Add_Product_id).first()
                if R_detele == None:
                      return {"message":"Request Not Fount"}
                else:
                      db.session.delete(R_detele)
                      db.session.commit()
            elif data["request"]=="Add Category":
                delet_Add_Category_id=data.get("Add_Category_id")
                print("success")

                R_detele = AddCategory.query.filter_by(R_id=delet_Add_Category_id).first()
                if R_detele == None:
                      return {"message":"Request Not Fount"}
                else:
                      db.session.delete(R_detele)
                      db.session.commit()
            elif data["request"]=="Edit Category":
                delet_Edit_Category_id=data.get("Edit_Category_id")
                R_detele = EditCategory.query.filter_by(R_id=delet_Edit_Category_id).first()
                if R_detele == None:
                      return {"message":"Request Not Fount"}
                else:
                      db.session.delete(R_detele)
                      db.session.commit()
            elif data["request"]=="Delet Delete_Category":
                delet_DeleteCategory_id=data.get("Delete_DeleteCategory_id")
                R_detele = DeleteCategory.query.filter_by(R_id=delet_DeleteCategory_id).first()
                if R_detele == None:
                      return {"message":"Request Not Fount"}
                else:
                      db.session.delete(R_detele)
                      db.session.commit()
                 
            elif data["request"]=="Delete Delete_Product":
                delet_DeleteProduct_id=data.get("Delete_DeleteProduct_id")
                R_detele = DeleteProduct.query.filter_by(R_id=delet_DeleteProduct_id).first()
                if R_detele == None:
                      return {"message":"Request Not Fount"}
                else:
                      db.session.delete(R_detele)
                      db.session.commit()

                 


        except Exception as e:
            print(e)
            return {'message' : "Internal Server Error"} , 500  
    

api.add_resource(TestimonialUserApi,'/testimonial')




# Role_requard funtion for asmin
def role_required(func):
    
    
    def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                try:
                    token = get_jwt_identity()
                    print(token)
                    if not token:
                        return {'Alert':"Token is missing"},403
                    user = User.query.filter_by(User_id = token["User_id"]).first();  
                    if not user:
                        return {'Alert':"User not  defind"},404
                    if not user.Role in func:
                        return {'msg' : 'Unauthorised.'} , 401

                    return fn(*args, **kwargs)
                
                except Exception as e:
                            print(e)
                            return {'msg' : 'Internal Server Error'} , 500
            return wrapper
    return decorator








class TestimonialAdminApi(Resource):
    '''
        API for testimonials of a general user
    '''
    @jwt_required()
    @role_required(['ADMIN'])
    def get(self):
        try :
           
            
            Add_Category = AddCategory.query.filter_by(R_approved = False).all()
            Dist_Add_Category = []
            if len(Add_Category) !=0:
                for i in range(len(Add_Category)):
                    Dist_Add_Category.append({"R_id":0,"R_Category_name":'',"R_approved":False,"R_user_id":0})

                for i in range(len(Dist_Add_Category)):
                        Dist_Add_Category[i]["R_id"]=Add_Category[i-1].R_id
                        Dist_Add_Category[i]["R_Category_name"]=Add_Category[i-1].R_Category_name
                        Dist_Add_Category[i]["R_approved"]=Add_Category[i-1].R_approved

                        Dist_Add_Category[i]["R_user_id"]=Add_Category[i-1].R_user_id





                    
          
            Edit_Category = EditCategory.query.filter_by(R_approved = False).all()
            #  Edit_Category = EditCategory.query.filter_by(R_user_id = user_id).all()
            Dist_Edit_Category = []
            
            if len(Edit_Category) !=0:

                for i in range(len(Edit_Category)):
                    Dist_Edit_Category.append({"R_id":0,"R_Category_name":'',"R_approved":False,"R_user_id":0})
                for i in range(len(Edit_Category)):
                        Dist_Edit_Category[i]["R_id"]=Edit_Category[i-1].R_id
                        Dist_Edit_Category[i]["R_Category_name"]=Edit_Category[i-1].R_Category_name
                        Dist_Edit_Category[i]["R_Category_id"]=Edit_Category[i-1].R_Category_id
                        Dist_Edit_Category[i]["R_approved"]=Edit_Category[i-1].R_approved

                        Dist_Edit_Category[i]["R_user_id"]=Edit_Category[i-1].R_user_id

                


            Add_Product = AddProduct.query.filter_by(R_approved = False).all()
            Dist_Add_Product = []
            
            if len(Add_Product) !=0:

            
                for i in range(len(Add_Product)):
                    Dist_Add_Product.append({"R_Product_id":0,"R_Category_id":0,"R_Productname":'',"R_Product_Unit":'',
                                        "R_Product_Qut":0,"R_price":0,"R_ProductExp":'',"R_image":'',"R_approved":False,"R_user_id":0})
                for i in range(len(Add_Product)):
                        Dist_Add_Product[i]["R_Product_id"]=Add_Product[i-1].R_Product_id
                        Dist_Add_Product[i]["R_Category_id"]=Add_Product[i-1].R_Category_id
                        Dist_Add_Product[i]["R_Productname"]=Add_Product[i-1].R_Productname
                        Dist_Add_Product[i]["R_Product_Unit"]=Add_Product[i-1].R_Product_Unit
                        Dist_Add_Product[i]["R_Product_Qut"]=Add_Product[i-1].R_Product_Qut
                        Dist_Add_Product[i]["R_price"]=Add_Product[i-1].R_price
                        Dist_Add_Product[i]["R_image"]=Add_Product[i-1].R_image
                        Dist_Add_Product[i]["R_approved"]=Add_Product[i-1].R_approved

                        Dist_Add_Product[i]["R_ProductExp"]=Add_Product[i-1].R_ProductExp
                        Dist_Add_Product[i]["R_user_id"]=Add_Product[i-1].R_user_id






            Edit_Product = EditProduct.query.filter_by(R_approved = False).all() 
            Dist_Edit_Product = []
          
            if len(Edit_Product) !=0:

                
                for i in range(len(Edit_Product)):
                    Dist_Edit_Product.append({"R_id":0,"R_Category_id":0,"R_Productname":'',"R_Product_Unit":'',
                                        "R_Product_Qut":0,"R_price":0,"R_ProductExp":'',"R_image":'',"R_Product_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Edit_Product)):
                        Dist_Edit_Product[i]["R_id"]=Edit_Product[i-1].R_id
                        # Dist_Edit_Product[i]["R_Product_id"]=Edit_Product[i-1].R_Product_id
                        Dist_Edit_Product[i]["R_Category_id"]=Edit_Product[i-1].R_Category_id
                        Dist_Edit_Product[i]["R_Productname"]=Edit_Product[i-1].R_Productname
                        Dist_Edit_Product[i]["R_Product_Unit"]=Edit_Product[i-1].R_Product_Unit
                        Dist_Edit_Product[i]["R_Product_Qut"]=Edit_Product[i-1].R_Product_Qut
                        Dist_Edit_Product[i]["R_price"]=Edit_Product[i-1].R_price
                        Dist_Edit_Product[i]["R_ProductExp"]=Edit_Product[i-1].R_ProductExp
                        Dist_Edit_Product[i]["R_image"]=Edit_Product[i-1].R_image

                        Dist_Edit_Product[i]["R_Product_id"]=Edit_Product[i-1].R_Product_id
                        Dist_Edit_Product[i]["R_approved"]=Edit_Product[i-1].R_approved

                        Dist_Edit_Product[i]["R_user_id"]=Edit_Product[i-1].R_user_id 

            Delete_Product = DeleteProduct.query.filter_by(R_approved = False).all()
            Dist_Delete_Product = []
          
            if len(Delete_Product) !=0:

                
                for i in range(len(Delete_Product)):
                    Dist_Delete_Product.append({"R_id":0,"R_Product_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Delete_Product)):
                        Dist_Delete_Product[i]["R_id"]=Delete_Product[i-1].R_id
                        Dist_Delete_Product[i]["R_Product_id"]=Delete_Product[i-1].R_Product_id
                        Dist_Delete_Product[i]["R_approved"]=Delete_Product[i-1].R_approved
                        Dist_Delete_Product[i]["R_user_id"]=Delete_Product[i-1].R_user_id  

            Delete_Category = DeleteCategory.query.filter_by(R_approved =False).all()
            Dist_Delete_Category = []
          
            if len(Delete_Category) !=0:

                
                for i in range(len(Delete_Category)):
                    Dist_Delete_Category.append({"R_id":0,"R_Product_id":0,"R_approved":False,"R_user_id":0})
                for i in range(len(Delete_Category)):
                        Dist_Delete_Category[i]["R_id"]=Delete_Category[i-1].R_id
                        Dist_Delete_Category[i]["R_Category_id"]=Delete_Category[i-1].R_Category_id
                        Dist_Delete_Category[i]["R_approved"]=Delete_Category[i-1].R_approved
                        Dist_Delete_Category[i]["R_user_id"]=Delete_Category[i-1].R_user_id            




            print(Delete_Category)
            print(Dist_Delete_Category)

            result = {
                'AddCategory' : Dist_Add_Category,
                'EditCategory' : Dist_Edit_Category,
                'AddProduct':Dist_Add_Product,
                'EditProduct' : Dist_Edit_Product,
                'DeleteProduct':Dist_Delete_Product,
                'DeleteCategory':Dist_Delete_Category,
            } 
            print(result)
            return result , 200
        except Exception as e :
            print(e)
            return {'message' : "Internal Server Error"} , 500
    
    @jwt_required()
    @role_required(['ADMIN'])
    def put(self):
        try:
            current_user = get_jwt_identity()
            data = request.get_json()
            
            request_A_E_P_C = data.get('request')
            request_id = data.get('request_id')

            status = data.get('status',False)
            user_id = current_user.get('User_id')

            try:
                request_id = data.get('request_id')
                status = bool(status)

            except Exception as e:
                print(e)
                return {'message' : "Invalid data in fields"} , 400
            
            if(user_id and request_id and request_A_E_P_C):
                
                if request_A_E_P_C == "Add Product":
                    testimonial = AddProduct.query.filter_by(R_Product_id = request_id).first()
                    if not testimonial:
                        return {'message': 'Request not found'}, 404
                    testimonial.R_approved = status
                    db.session.commit()
                
                    return {"message" : "Successfully Updated"} , 200
                elif request_A_E_P_C == "Edit Product" :    
                    testimonial = EditProduct.query.filter_by(R_id  = request_id).first()
                    if not testimonial:
                        return {'message': 'Request not found'}, 404
                    testimonial.R_approved = status
                    db.session.commit()
                
                    return {"message" : "Successfully Updated"} , 200
                elif request_A_E_P_C == "Add Category":  
                    testimonial = AddCategory.query.filter_by(R_id = request_id).first()
                    if not testimonial:
                        return {'message': 'Request not found'}, 404
                    testimonial.R_approved = status
                    db.session.commit()
                
                    return {"message" : "Successfully Updated"} , 200


                elif request_A_E_P_C == "Edit Category":      
                    testimonial = EditCategory.query.filter_by(R_id = request_id).first()
                    if not testimonial:
                        return {'message': 'Request not found'}, 404
                    testimonial.R_approved = status
                    db.session.commit()
                
                    return {"message" : "Successfully Updated"} , 200
                
                elif request_A_E_P_C == "Delete Delete_Category":      
                    testimonial = DeleteCategory.query.filter_by(R_id = request_id).first()
                    if not testimonial:
                        return {'message': 'Request not found'}, 404
                    testimonial.R_approved = status
                    db.session.commit()
                
                    return {"message" : "Successfully Updated"} , 200
                elif request_A_E_P_C == "Delete Delete_Product":      
                    testimonial = DeleteProduct.query.filter_by(R_id = request_id).first()
                    if not testimonial:
                        return {'message': 'Request not found'}, 404
                    testimonial.R_approved = status
                    db.session.commit()
                
                    return {"message" : "Successfully Updated"} , 200
                

                    

            else:
                return {'message': 'Missing details'}, 400

        except Exception as e:
            print(e)
            return {'message' : "Internal Server Error"} , 500
    

api.add_resource(TestimonialAdminApi,'/admin/testimonial')










class Category_manage(Resource):
    @marshal_with(all_cates)
    def get(self):
        cates = Category.query.all()
        return cates
    
    def post(self):
        args = cate_parser.parse_args()
        cate_name = args['name']
        cate_user_id = args['user_id']
        if cate_name  and cate_user_id :
                cates = Category.query.filter_by( Categoryname = cate_name ).first()
            
                print(cates)
                if cates == None  :
                    new_cate = Category(Categoryname=cate_name,buy_id=cate_user_id)
                    db.session.add(new_cate)
                    db.session.commit()
                    return {'massage':'Category add successfully'}

                error = f"{cate_name}, is already exist!"
                return {'massage':error}
                
    
        else:
            
            return {'massage':'Please fill out the category! name and user_id'} 
              
                                 
        
    def put(self):
        args = cate_parser.parse_args()
        cate_id = args['id']
        cate_name = args['name']
        if cate_name and cate_id:
            cate = Category.query.get(cate_id)
            cate.Categoryname = cate_name
            db.session.commit()
            return {'massage':'Category update successfully'}
        else:
            return {'massage':'Please, fill out category name! for change name '}

        

    def delete(self):
        args = cate_parser.parse_args()
        id = args['id']
        cate = Category.query.get(id)
        if cate:

            prods = Product.query.filter_by(Category_id=id).all()

            if prods:
              

                for prod in prods:
                    db.session.delete(prod)
                    db.session.commit()
            db.session.delete(cate)
            db.session.commit()  
            return {'massage':'Category deleted successfully'}
              
        else:
            

            db.session.delete(cate)
            db.session.commit()
            return {'massage':'Category deleted successfully'}



class Product_manage(Resource):
    @marshal_with(all_prods)
    def get(self):
        prods = Product.query.all()
        return prods

    def post(self):
        print('from post')
        args = prod_parser.parse_args()
        name = args['name']
        qnt = args['qnt']
     
        exp_date = args['exp_date']
        price = args['price']
        nop = args['nop']
        cate_id = args['cate_id']
        image = args['image']

        if name and qnt and exp_date and price and nop and cate_id and image and qnt:

                new_prod = Product(Productname=name,
                                    Product_Unit=qnt,
                                    
                                    ProductExp=exp_date,
                                    price=price,
                                    Product_Qut=nop,
                                    image=image,
                                    Category_id=cate_id
                                    )
                
                db.session.add(new_prod)
                db.session.commit()
                return {'massage':'Product add successfully'}
        else:

            return {'massage':'Provide all Details of Product','Detail':'name and qnt and exp_date and price and nop cate_id and image'}




    def put(self):
        args = prod_parser.parse_args()
        prod_id = args['id']
        name = args['name']
        qnt = args['qnt']
        mfg_date = args['mfg_date']
        exp_date = args['exp_date']
        price = args['price']
        nop = args['nop']
        image = args['image']
        cate_id = args['cate_id']
        
        if prod_id:
            prod = Product.query.filter_by(Product_id=prod_id).first()
            print("upadet",prod)
            
            if name !='':
                prod.Productname = name
                
            if qnt !="" or qnt!=0:
                prod.Product_Unit = qnt
            if exp_date !='':
                prod.ProductExp = exp_date
            if   price != '' :
                print(type(price))
                prod.price =price
            if   nop != "" :
                print("nop",type(nop))
                prod.Product_Qut = int(nop)
            if   image !='':   
                prod.image = image
            if   cate_id != None  :
                print("cate",type(cate_id))
                prod.Category_id = cate_id

            db.session.commit()
            return {'massage':'Product update successfully'}
        else:
             return {'massage':'Please provide prod_id first and then value for change'}

    def delete(self):
        args = prod_parser.parse_args()
        prod_id = args['id']
        prod = Product.query.get(prod_id)
        if prod:
            db.session.delete(prod)
            db.session.commit()
            return {'massage':'Product deleted successfully'}
        else:
            return {'massage':'Product Not found'}
             


#card Detail
class buyproduct(Resource):
    # @marshal_with(all_cart)
    # def get(self):
    #     args = card_parser.parse_args()
    #     user_id = args['user_id']
    #     prods = Cart.query.filter_by(user_id=user_id).all()
    #     return prods



    def post(self):
        print('buyprod post')
        
        data = request.get_json()

        # print(data.get("Buy_product"))
        buy_product=data.get("Buy_product")
        user=User.query.filter_by(Username=data.get("username")).first()
        current_time = datetime.datetime.now()
        user.datetime=current_time
        db.session.add(user)
        db.session.commit()

        print("User_id",user.User_id)
        if user:
            for i in range(len(buy_product)):
                
                    
                    new_prod = BuyProduct(User_id=user.User_id,Product_id=buy_product[i]["Product_id"],Category_id=buy_product[i]["Category_id"],Quantity=1
                                ,Price=buy_product[i]["price"],Total=buy_product[i]["price"])                
                    db.session.add(new_prod)
                    db.session.commit()
            return {"message":"Payment success"}
        else:
             return {"message":"User Notfound Singin"}



    




api.add_resource(Category_manage, '/api/category')
api.add_resource(Product_manage, '/api/product')
# api.add_resource(Card_manage, '/api/cart')
api.add_resource(UserRagistration, '/api/userragister')
api.add_resource(UserLogin, '/api/userLogin')
api.add_resource(buyproduct, '/api/buyproduct')



# {
#   "request":"Add Product",
#   "name":"Almond Oil",
#   "qnt":"pr",
#   "exp_date":"2023-09-20",
#   "price":200,
#   "nop":100,
#   "cate_id":1,
#   "image":"image/ands/##$/dtf.sr/frtwer"
  
# }

# {
#   "request":"Edit Category",
#   "Category_id":1,
#   "Category_name":"Break Fast"
# }

# {
#   "request":"Edit Category",
#   "Category_id":1,
#   "Category_name":"Break Fast"
# }