import csv
import os
from application.models import User,Category,Product,BuyProduct,Cart,db,AddCategory,EditCategory,AddProduct,EditProduct,DeleteProduct,DeleteCategory


from application.send_mail import sendMail
from datetime import datetime


def export_testimonial_data():
    try:
        products=Product.query.all()
        print("before make csv",products)
        # Get the admin from database
        user = User.query.filter_by(Role='ADMIN').first()

        current_time = datetime.now()
        date_time = current_time.strftime("%m_%d_%Y%H_%M_%S")
        print("date and time:",date_time, type(date_time))
        # "My name is {0}, I'm {1}".format("John",36)
        print("file_path", type(current_time))

        file_path = "report/report_product_export_"+date_time + ".csv"
        # Write the content in the file
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['Product_id', 'Category_id','Productname',"Product_Unit",
                          "Product_Qut","price","ProductExp"]  # Replace with the actual column names in your Testimonial table
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
# "Product_id","Category_id","Productname","Product_Unit","Product_Qut","price","ProductExp","image"

            for product in products:
                print(product,"product")
                writer.writerow({
                    'Product_id': product.Product_id, 
                    'Category_id': product.Category_id, 
                    'Productname' : product.Productname, 
                    'Product_Unit':product.Product_Unit,
                    'Product_Qut':product.Product_Qut,
                    'price':product.price,
                    'ProductExp':product.ProductExp
                    
                })
            # print("before make csv",products.Product_id)


        # Send the email to admin with the csv file in atatchment
        # res = sendMail(user.Username,"Monthly Report","The Report has been exported and attached below.",file_path,"text/csv")
        return file_path
    except Exception as e:
        print(e)
        return False
    

# Monthly Report 

# def monthlyreport_data():
#     try:
       
#         user = User.query.filter_by(Role='user').first()
#         products=BuyProduct.query.filter_by(User_id=user.User_id).first()


#         current_time = datetime.now()
#         date_time = current_time.strftime("%m_%d_%Y%H_%M_%S")
#         print("date and time:",date_time, type(date_time))
#         # "My name is {0}, I'm {1}".format("John",36)
#         print("file_path", type(current_time))

#         file_path = "report/monthly_product_export_"+date_time + ".csv"
#         # Write the content in the file
#         with open(file_path, 'w', newline='') as csv_file:
#             fieldnames = ['Username', 'Category_id','Productname',"Product_Unit",
#                           "Product_Qut","price","ProductExp"]  # Replace with the actual column names in your Testimonial table
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             writer.writeheader()
# # "Product_id","Category_id","Productname","Product_Unit","Product_Qut","price","ProductExp","image"

#             for product in products:
#                 print(product,"product")
#                 writer.writerow({
#                     'Product_id': product.Product_id, 
#                     'Category_id': product.Category_id, 
#                     'Productname' : product.Productname, 
#                     'Product_Unit':product.Product_Unit,
#                     'Product_Qut':product.Product_Qut,
#                     'price':product.price,
#                     'ProductExp':product.ProductExp
                    
#                 })
#             # print("before make csv",products.Product_id)


#         # Send the email to admin with the csv file in atatchment
#         # res = sendMail(user.Username,"Monthly Report","The Report has been exported and attached below.",file_path,"text/csv")
#         return file_path
#     except Exception as e:
#         print(e)
#         return False