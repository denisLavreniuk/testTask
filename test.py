import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string


def send_mail():
    login="asferrotest@gmail.com"
    password="asferro123"
    url="smtp.gmail.com"
    toaddr=login
    topic=''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
    message=''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
    num = 15

    for value in range (num):
        msg=MIMEMultipart()

        msg[ 'Subject' ]=topic
        msg[ 'From' ]=login
        body =message
        msg.attach( MIMEText( body, 'plain'))

        server = root.SMTP_SSL(url,465)
        server.login( login, password )
        server.sendmail( login, toaddr, msg.as_string())
        value+=1
        print('Отравлено: '+str(value))

def main():
    send_mail()

if __name__ == '__main__':
    main()