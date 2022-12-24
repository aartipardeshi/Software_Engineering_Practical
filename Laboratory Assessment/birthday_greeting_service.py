#Implemenrt at least three features for birthday greeting server application


import datetime
import imghdr
import mysql.connecter
import os
import pywhatkit as pwt
import smtplib
from email.message import EmailMessage


now= str(datetime.date.today())
#for input date and time in format like ddmm
today = now[8:10] +now[5:7]
print(now)
