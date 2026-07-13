'''
SMTP module
email.message
jxdo faon fkzf cxat
'''
import smtplib
from email.message import EmailMessage
sender_email = "kusumapriya2005@gmail.com"
password = "jxdofaonfkzfcxat"
receiver_email = "dosapatrunikusumapriya@gmail.com,sanjanasaraswathi7799@gmail.com"
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = "welcome Mail"
message.set_content(f"""Hello KUSUMA! welcome to our python class
                     regards,
                     python team""")
try:
    
    smtp = smtplib.SMTP("smtp.gmail.com",port=587)
    smtp.starttls()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    print("Email sent successfully")
except Exception as e:
    print("Error: ",e)
finally:
    smtp.quit()
    
