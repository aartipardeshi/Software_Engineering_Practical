#Program for OTP generate and send OTP using functional decomposition

import random
import re
import smtplib
import time

#For generate OTP:
size = random.randint(4,10)
def generate_otp(size):
    otp=''
    for i in range(size):
          val=random.randint(0,9)
          otp = otp + str(val)
    return (otp)


# For validation of Email:
def check(email):
    s = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if (re.search(s, email)):
        print("Email is valid.")
        return True
    else:
        print("Email is not valid.\n Please enter valid Email.")
        return False

    
#For sending OTP:
def send_otp(mail,otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    password = 'wjhe gkxm zueo wrmc'
    sender_mail = "pardeshiaarti49@gmail.com"
    msg = ' Hello, Your OTP is ' + str(otp)
    server.login(sender_mail,password)
    server.sendmail('pardeshiaarti49@gmail.com', mail, msg)
    print("OTP send!")
    server.quit()


email= 'pardeshiaarti49@gmail.com'
if(check(email)):

    size = random.randint(4,10)
    otp = generate_otp(size)
    send_otp(email,otp)


