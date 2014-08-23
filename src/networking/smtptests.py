__author__ = 'proSingularity'

import smtplib

s = smtplib.SMTP()
s.connect("smtp.mail.yahoo.com", 465)
print("connected")
s.login("53453", "stuff")