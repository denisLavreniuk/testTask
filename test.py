import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail():
    #login=input('введите почту: ')
    login="asferrotest@gmail.com"
    #password=input('введите пароль: ')
    password="asferro123"
    #url=input('введите URL: ')
    url="smtp.gmail.com"
    #toaddr=input('кому: ')
    toaddr=login
    topic=input('тема: ')
    message=input('введите сообщение: ')
    num = int(input('количество сообщений: '))

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