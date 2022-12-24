import random
import re
import smtplib

# For validation of Email
def check(email):
    s = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if (re.search(s, email)):
        print("Email is valid.")
    else:
        raise AssertionError(email +" is not valid Email.")
                             
        

#For generate OTP

def generate_otp(size):
    otp=''
    for i in range(size):
          val=random.randint(0,9)
          otp = otp + str(val)
    return (otp)

#For Checking length of otp:
def otp_length(otp):
    if not (4<= len(otp) <=10):
        raise AsserionError("Length of OTP should be in between 4 and 10")
    else:
        print("Length of OTP is valid!")


#For sending OTP
def send_otp(mail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    password = 'wjhe gkxm zueo wrmc'
    sender_mail = "pardeshiaarti49@gmail.com"
    otp = generate_otp(size)
    msg = ' Hello, Your OTP is ' + str(otp)
    server.login(sender_mail,password)
    server.sendmail('pardeshiaarti49@gmail.com', mail, msg)
    server.quit()
    print("OTP send!")


