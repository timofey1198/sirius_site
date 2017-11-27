# -*- coding: utf-8 -*-
import smtplib

def Mail(to, message):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    print(smtp_obj.starttls())
    smtp_obj.login('', '')
    smtp_obj.sendmail('timostar98@gmail.com', to, message)
    smtp_obj.quit()
