import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://gmail.com/')



def login():
    textarea = browser.find_element_by_id('identifierId')
    textarea.send_keys("asferrotest@gmail.com")
    textarea.send_keys(Keys.ENTER)
    time.sleep(1)
    textarea2 = browser.find_element_by_name('password')
    textarea2.send_keys('asferro123'+"\n")



def sendMail():
    global login 
    login = "asferrotest@gmail.com"
    global password
    password = "asferro123"
    global url 
    url = "smtp.gmail.com"
    global toaddr
    toaddr = login
    num = 15

    for value in range(num):
        topic = ''.join(random.choice(string.ascii_letters +string.digits) for i in range(10))
        message = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))

        msg = MIMEMultipart()

        msg['Subject'] = topic
        msg['From'] = login
        body = message
        msg.attach(MIMEText(body, 'plain'))

        global server
        server = root.SMTP_SSL(url, 465)
        server.login(login, password)
        server.sendmail(login, toaddr, msg.as_string())
        value += 1
        print('Сообщение '+str(value)+' доставлено')


def getMessages(browser):
    global dictionary
    dictionary = {"key": "value"}
    print(dictionary)
    k = browser.find_elements_by_xpath("//div[@class='UI']//table//tbody/tr//following-sibling::td[5]//span[@class='bog']/span")
    v = browser.find_elements_by_xpath("/html[1]/body[1]/div[7]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]//td[6]/div[1]/div[1]/span[1]")
    for x in k:                 
        print(x.text)
        for y in v:
            dictionary.update({x.text: y.text})
            # print(y.text)
            print(dictionary)


def getReport():
    for key in dictionary:
        print ("%s -> %s" % (key, dictionary[key]))
        numberOfDigits=("%s" % (dictionary[key]))
        cnt=0
        for s in numberOfDigits:
            if s.isdigit():
                cnt+=1
        if cnt:
            print(cnt)
        else:
            print("числа не обнаружены")


        word = "%s" % (dictionary[key])
        numberOfLetters=0
        for i in word:
                if 'a' <= i <= 'z'or 'A' <= i <= 'Z':
                        numberOfLetters += 1                         
        mes = MIMEMultipart()
        print(key)
        mess= 'Received mail on theme ' +("%s" % (key))+' with message: ' +("%s" % (dictionary[key]))+'. It contains ' +str(numberOfLetters)+ ' letters and '+ str(cnt) +' numbers.'
        print('mess= '+mess)
        print(mess)
        m=''
        m+=mess
    print('m=======       '+m)
    mes['From'] = login
    body = str(mess)
    mes.attach(MIMEText(body, 'plain'))

    server.login(login, password)
    server.sendmail(login, toaddr, str(mess))

def delete():
    browser.find_element_by_id(':2l').click()
    time.sleep(1)

    browser.find_element_by_id(':2t').click()
    time.sleep(2)

    browser.find_element_by_xpath("*//div[@class='T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA']").click()
    time.sleep(2)



def getDict():
    r={}
    while (True):
        print('Enter key (empty enter - exit)')
        k=input()
        if k=='':
            break
        print('Enter value')
        v=input()
        r[k]=v
    print(r)
    return r


def main():
    login()
    sendMail()
    browser.refresh()
    time.sleep(5)
    getMessages(browser)
    getReport()
    delete()
    browser.close()



if __name__ == '__main__':
    main()