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



def sendMail():
    login="asferrotest@gmail.com"
    password="asferro123"
    url="smtp.gmail.com"
    toaddr=login
    num = 5

    for value in range (num):
        
        topic=''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
        message=''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))  

        d={}
        for a in range(num):
            d[topic]=message#dict
            k=str(topic)+str(message)
            d[k]=a
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
        
def getMessages(browser):
    global dictionary
    dictionary = {"key":"value"}
    print(dictionary)
    k=browser.find_elements_by_xpath("//div[@class='UI']//table//tbody/tr//following-sibling::td[5]//span[@class='bog']/span")
    v=browser.find_elements_by_xpath("/html[1]/body[1]/div[7]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/div[1]/span[1]")
    for x in k:
        for y in v:
            dictionary.update({x.text:y.text})
    print(dictionary)

def sendReport():
    print(dictionary)




def delete():
    browser.find_element_by_id(':2l').click()
    time.sleep(1)

    browser.find_element_by_id(':2t').click()
    time.sleep(2)

    browser.find_element_by_xpath("*//div[@class='T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA']").click()
    time.sleep(2)




def main():
    login()
    sendMail()
    browser.refresh()
    time.sleep(5)
    getMessages(browser)
    sendReport()
    delete()
    browser.close()
    

if __name__ == '__main__':
    main()