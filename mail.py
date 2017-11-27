import smtplib

def Mail(to, message):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    print(smtp_obj.starttls())
    smtp_obj.login('xxx@ccc.xx', 'pass')
    smtp_obj.sendmail('xxx@ccc.xx', to, message)
    smtp_obj.quit()
