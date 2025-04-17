from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import datetime
 
# using now() to get current time
current_time = datetime.datetime.now()


engin=None
Base = declarative_base()
db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'  # Corrected table name definition
    User_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emailid = db.Column(db.String, nullable=False)
    Username = db.Column(db.String, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Role = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True)
    datetime = db.Column(db.DateTime, default=current_time)
    
    # Establishing a relationship with the User_address model
    addresses = db.relationship('User_address', backref='user', lazy=True)
    Category = db.relationship('Category', backref='user', lazy=True)
        # One-to-many relationship with the shopping cart
    cart = db.relationship('ShoppingCart', backref='user', lazy=True)


class User_address(db.Model):
    __tablename__ = 'addresses'  # Corrected table name definition
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pincode = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    landmark = db.Column(db.String, nullable=False)
    datetime = db.Column(db.DateTime, default=current_time)
    user_id = db.Column(db.Integer, db.ForeignKey('users.User_id'), nullable=False)

# All Category Store here
class Category(db.Model):
    __titlename__="category"
    Category_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Categoryname = db.Column(db.String,nullable=False)
    User_id = db.Column(db.Integer,db.ForeignKey('users.User_id'), nullable=False)
    datetime = db.Column(db.DateTime())
    # Establishing a relationship with the Category model
    product = db.relationship('Product', backref='category', lazy=True)

# product Model 
class Product(db.Model):
    __titlename__="product"
    Product_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Productname = db.Column(db.String)
    Unit = db.Column(db.String)
    Qut = db.Column(db.Integer)
    price=db.Column(db.Integer)
    MFG = db.Column(db.String)
    Exp = db.Column(db.String)
    image = db.Column(db.String)
    datetime = db.Column(db.DateTime())
    Category_id = db.Column(db.Integer,db.ForeignKey('category.Category_id'))
    # Establishing a relationship with the Product model
    buyProduct = db.relationship('BuyProduct', backref='Product',lazy=True)
    cart_items = db.relationship('CartItem', backref='product', lazy=True)
# Request models 
class requestCategory(db.Model):
    __titlename__="requestCategory"
    R_id = db.Column(db.Integer, primary_key=True)
    R_C_name = db.Column(db.String(255))
    R_C_type = db.Column(db.String(255))
    R_approved = db.Column(db.Boolean, default=False)
    R_user_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime())   

#Add Product Model for Maneger request to Admin
class requestProduct(db.Model):
    __titlename__="AddProduct"

    R_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    R_C_id = db.Column(db.Integer,db.ForeignKey('category.Category_id'))
    R_P_id = db.Column(db.Integer)
    R_P_name = db.Column(db.String)
    R_Unit = db.Column(db.String)
    R_Qut = db.Column(db.Integer)
    R_price=db.Column(db.Integer)
    R_MFG = db.Column(db.String)
    R_Exp = db.Column(db.String)
    R_image = db.Column(db.String)
    R_approved = db.Column(db.Boolean, default=False)
    R_P_type = db.Column(db.String(255))
    datetime = db.Column(db.DateTime())
    R_user_id = db.Column(db.Integer, db.ForeignKey('users.User_id'))
    user = db.relationship('User', backref='Product', lazy=True) #Testimonial Model for Maneger request to Admin

      
#Store Data of user 
class BuyProduct(db.Model):
    __titlename__="buyProduct"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    Price = db.Column(db.Integer)
    Total = db.Column(db.Integer)   
    datetime = db.Column(db.DateTime())
    User_id = db.Column(db.Integer,db.ForeignKey('users.User_id'))
    Category_id = db.Column(db.Integer,db.ForeignKey('category.Category_id'))
    Product_id = db.Column(db.Integer,db.ForeignKey("product.Product_id"))
    Quantity = db.Column(db.Integer)

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.User_id'), nullable=False)
    created_at = db.Column(db.DateTime)

    # One-to-many relationship with CartItem
    items = db.relationship('CartItem', backref='cart', lazy=True)


class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('shopping_cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.Product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    added_at = db.Column(db.DateTime)

    # Calculated field for the total price of the item (product price * quantity)
    @property
    def total_price(self):
        return self.product.price * self.quantity