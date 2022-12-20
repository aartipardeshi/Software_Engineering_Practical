#Program for generating and sending otp without functional decompositon.


import random
import smtplib

otp = random.randint(1000,9999)
server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
server.starttls()

#This is 2-step generate password
password = 'wjhe gkxm zueo wrmc'

server.login('pardeshiaarti49@gmail.com',password)
msg = ' Hello, Your OTP is '+str(otp)
mail=str(input("Enter the mail:"))
server.sendmail('pardeshiaarti49@gmail.com',mail, msg)
server.quit()
