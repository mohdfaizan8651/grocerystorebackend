from application.models import User,BuyProduct
from application.send_mail import sendMail
import datetime
 
# using now() to get current time


def monthlyreport():
    try:

        Users= User.query.all()

        # # Set the message to send

        for i in range(len(Users)):
            products=BuyProduct.query.filter_by(User_id=Users[i].User_id).all()
            Total=0
            for i in range(len(products)):
                Total +=products[i].Total
            
            print(Total,type(Total))
         

            message = "Total Expenditure in a Month:" + str(Total )
            res = sendMail(Users[i].Username,"Your Monthly Expenditure",message)
    

                
        return res
    except:
        return False
    
def send_remainder_emails():
    try:

        Users= User.query.all()

        # # Set the message to send

        for i in range(len(Users)):
                current_time = datetime.datetime.now()

            # if((current_time-Users[i].datetime).total_seconds()>14400):
                print("Diffrence date ",current_time-Users[i].datetime)

                message = "Visit Grocary Store and Buy Something "
                res = sendMail(Users[i].Username,"Reminder for Visit and Buy items",message)
    

                
        return res
    except:
        return False