# -*- coding:utf-8 -*-
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header
from traceback import print_exc

success_msg='''\
<html>  
    <body>
        <h3>欢迎注册Lemonbook</h3>
        <p>
        Hi.{{ current_user.username }}<br/>
        Thanks for registering Lemonbook! I hope it will bring you pleasure and good luck.<br/>
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
    mail_host = 'smtp.gmail.com:587'
    v_username = ''
    v_password = ''
    server = smtplib.SMTP(mail_host)
    server.starttls()
    server.login(v_username, v_password)
    server.sendmail(sender, receivers, msg.as_string())
    server.quit()
            
