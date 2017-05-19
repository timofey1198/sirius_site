import smtplib

def Mail(to, message):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    print(smtp_obj.starttls())
    smtp_obj.login('timostar98@gmail.com', 'Upiter98112358132134')
    smtp_obj.sendmail('timostar98@gmail.com', to, message)
    smtp_obj.quit()