import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG=False
    SQLITE_DB_DIR=None
    SQLALCHEMY_DATABASE_URI=None
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    WTF_CSRF_ENABLED = False
  

class LocalDevelopmentConfige(Config):

    # Configration of Database

    SQLITE_DB_DIR=os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join(SQLITE_DB_DIR, "DATABASE_PROJECT_2.sqlite3")
    DEBUG=True

    #Celery Initialization
    CELERY_BROKER_URL='redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
    ENABLE_UTC = False
    TIMEZONE = "Asia/Calcutta"

    # Sccrit Key For token
    SECRET_KEY='c229cd5e2e4a47ccb6a550d744fbb5fc'
    
    #JWT Token
    JWT_TOKEN_LOCATION=["headers"]

    #Mail initialization
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'mohdfaizan8651@gmail.com'
    MAIL_PASSWORD = 'yizd fbfy befe uxxz'

#Gmail Passwords for other app
#yizd fbfy befe uxxz
       