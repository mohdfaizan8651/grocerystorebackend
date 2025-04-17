from celery import Celery
celery = Celery()
from celery.schedules import crontab

#Perodic task 
@celery.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
#      sender.add_periodic_task(10.0, test.s(), name='add every 10')
    # pass
    # sender.add_periodic_task(10,add.s(2,2),name="A remainder email to all those who have not updated the logs today")
     sender.add_periodic_task(crontab(hour=10, minute=43, day_of_week=7),remainder_emails.s(),name="A remainder email to approve testimonials.")
    #  sender.add_periodic_task(20,remainder_emails.s(),name="A remainder email to approve testimonials.")
    #  sender.add_periodic_task(30,expenditureremainder_emails.s(),name="Monthly expenditure   email .")


#     return x + y


from application.remainder_mail import send_remainder_emails,monthlyreport

@celery.task(name="send remainder emails")
def remainder_emails():
    res = send_remainder_emails()
    
    if(res): 
        print("after if",res)
        
        return 'Successfully Sent'
    else : 
        print("Else part",res)
        
        return 'Failed to send'
    
@celery.task(name="send monthly expenditure emails")
def expenditureremainder_emails():
    res = monthlyreport()
    
    if(res): 
        print("after if",res)
        
        return 'Successfully Sent'
    else : 
        print("Else part",res)
        
        return 'Failed to send'


from application.export_csv import export_testimonial_data

@celery.task(name="send Manegre Csv ")
def ManegerReport_csv():
    res = export_testimonial_data()
    print(res)
    if(res): 
        print('Successfully Sent Monthly Report',res)
        
        return res
    else : 
        print("Else part",res)
        
        return 'Failed to Sent Monthly Report send '



# pip install gevent

# celery -A my_project_name worker --pool=solo -l info



# Celery Worker : celery -A main.cel worker --loglevel=info
# Celery Beat : celery -A main.cel beat --loglevel=info
# Redis : sudo service redis-server start
# To check if redis is running : redis-cli ping If it return PONG, means redis is runnning