import smtplib

def send_email_alert(msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", "receiver@gmail.com", msg)
    server.quit()
