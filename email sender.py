from email.message import EmailMessage  #for email ralated works
import ssl                              #to encrypt the transport from client side-to server side
import smtplib                          #object that can be used to send mails to any Internet machine with an SMTP
sender='abc@gmail.com'#your email id
password= "abcdefghjso"#your email security key after creating a variable

receiver='receiver@gmail.com'

subject="this is a email sender python project"
body="""
this is my first project of my series
"""

em=EmailMessage()
em['From']=sender
em['to']=receiver
em['subject']=subject
em.set_content(body)            #used to set content in a body box in email

context=ssl.create_default_context() #  In Python, the ssl.create_default_context function is used to create an SSL (Secure Sockets Layer) context with a set of default settings suitable for secure communication

# Establish a secure connection to the SMTP server (in this case, Gmail)
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,em.as_string())
           