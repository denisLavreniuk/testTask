import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Chrome()
browser.get('https://gmail.com/')



def login():
    textarea=browser.find_element_by_id('identifierId')
    textarea.send_keys("asferrotest@gmail.com")
    textarea.send_keys(Keys.ENTER)
    time.sleep(1)
    textarea2=browser.find_element_by_name('password')
    textarea2.send_keys('asferro123'+"\n")



def send_mail():
    login="asferrotest@gmail.com"
    password="asferro123"
    url="smtp.gmail.com"
    toaddr=login
    num = 1

    for value in range (num):
        


        d = {'key': 'value'}
        for a in range(num):  
            topic=''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
            message=''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))  
            
            d[topic]=message
            print(d)

            msg=MIMEMultipart()

            msg[ 'Subject' ]=topic
            msg[ 'From' ]=login
            body =message
            msg.attach( MIMEText( body, 'plain'))

            server = root.SMTP_SSL(url,465)
            server.login( login, password )
            server.sendmail( login, toaddr, msg.as_string())
            value+=1
            print('Сообщение '+str(value)+' доставлено')

def main():
    login()
    send_mail()
    

if __name__ == '__main__':
    main()