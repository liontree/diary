# -*- coding:utf-8 -*-
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header
from traceback import print_exc
from string import Template
from lemonbook.config import MAIL_HOST,MAIL_USERNAME,MAIL_PASSWORD


success_msg='''\
<html>  
    <body>
        <h3>welcome to Lemonbook</h3>
        <p>
        Hi. %s<br/>
        Thanks for registering Lemonbook! I hope it will bring you pleasure and good luck.<br/>
        Click to below address to complete registration.<br/>
        http://*******<br/>
        If the url can not be clicked, please copy it to your browser address bar.<br/>
        Please enjoying it.<br/>
        </p><br/><br/><br/>
        <p>
        This email is sending from system automatically, please do not reply.
        <br/>Thanks
        </p>
    </body>
</html>
'''

def send_mail(sender,receiver,title,content):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(title, 'utf-8')
    try:
        msg.attach(MIMEText(content, 'html', 'utf-8'))
    except:
        print_exc()

    import smtplib
    mail_host = MAIL_HOST
    v_username = MAIL_USERNAME
    v_password = MAIL_PASSWORD
    server = smtplib.SMTP(MAIL_HOST)
    server.starttls()
    server.login(v_username, v_password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()
            
