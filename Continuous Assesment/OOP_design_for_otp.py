#Program for OOP design for generating and sending otp.


import random
import re
import smtplib
import time

class service_otp:
    #constructor
    def __init__(self,email,size):
        self.email = email
        self.size = size
        self.check()
        otp_no = self.generate_otp()
        self.send_otp(otp_no)


    # For validation of Email:
    def check(self):
        s = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if (re.search(s,self.email)):
            print("Email is valid.")

        else:
            print("Email is not valid.")


    # For generate OTP:
    def generate_otp(self):
        otp = ''
        for i in range(self.size):
            val = random.randint(0, 9)
            otp = otp + str(val)
        return (otp)

    # For sending OTP
    def send_otp(self,otp):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        password = 'wjhe gkxm zueo wrmc'
        sender_mail = "pardeshiaarti49@gmail.com"
        self.otp = otp
        msg = ' Hello, Your OTP is ' + str(self.otp)
        server.login(sender_mail, password)
        server.sendmail('pardeshiaarti49@gmail.com', self.email, msg)
        print("OTP send!")
        server.quit()


size = random.randint(4,10)

object= service_otp("pardeshiaarti49@gmail.com", size)




