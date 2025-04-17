from flask import Flask ,render_template,request
from application.models import *
import os 
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfige
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash
from celery.result import AsyncResult
# from application import tasks 
# from celery.schedules import crontab
# from celery import Celery
# from application.tasks import celery 
from flask_cors import CORS
# from application.mail import mail






def create_app():
    app=Flask(__name__,template_folder="templates")
    if os.getenv("ENV","development") == "production":
         raise Exception("currently  no production config is setup")
    else:
        print("Starting from Local Development")
        app.config.from_object(LocalDevelopmentConfige)
    db.init_app(app)
    app.app_context().push()



    # celery.conf.broker_url = app.config["CELERY_BROKER_URL"]
    # celery.conf.result_backend = app.config["CELERY_RESULT_BACKEND"]
    # celery.conf.enable_utc = app.config["ENABLE_UTC"]
    # celery.conf.timezone = app.config["TIMEZONE"]

    # class ContextTask(celery.Task):
    #     def __call__(self, *args, **kwargs):
    #         with app.app_context():
    #             return self.run(*args, **kwargs)

    # celery.Task = ContextTask


    app.app_context().push()
    # jwt = JWTManager(app)
    JWTManager(app)
    app.app_context().push()
    CORS(app)
    # mail.init_app(app)
    app.app_context().push()
    # import yourapplication.views
    return app





def initialise_database():
   with app.app_context():

        inspector = db.inspect(db.engine)
        table_names = inspector.get_table_names()

        if not table_names: 

            db.create_all()
            adminUser = User(Username="MOHD FAIZAN ALI",emailid="mohdfaizan8651@gmail.com",Password=generate_password_hash("password"),Role="ADMIN",active=True)
            db.session.add(adminUser)
            db.session.commit()

            print("Database tables created.")
        else:
            print("Database tables already exist.")



app=create_app()
initialise_database()




from application.controler import *
# from application.send_mail import *

# from api import *
if __name__=="__main__":
    app.run(debug=True)