#python email automation script

import smtplib
from email.mime.text import MIMEText

sender_email = "ashokabairwa382@gmail.com"
recipient_email = "ashokabairwa382@gmail.com"

subject = "Automated email"
message = "This is automated email sent using python"


#smtp server configuration 

smpt_server = "smtp.gmail.com"
smtp_port = 587
smpt_username ="Ashoka_bairwa"
smpt_password = "274652"


msg = MIMEText(message)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email
try:
     server = smtplib.SMTP(smpt_server, smtp_port)
     server.starttls()
     server.login(smpt_username, smpt_password)
     server.sendmail(sender_email,recipient_email,msg.as_string())
     print("Email has been sent")


except Exception as e:
     print ("Error Sending Email : ",str(e))

finally
     server.quit()