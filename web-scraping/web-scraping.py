"""Script to trigger a mail when price of Amazon FireTVStick falls down."""
import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Amazon-FireTVStick-Alexa-Voice-Remote-Streaming-Player/dp/B0791YHVMK/ref=sr_1_1?crid=35GK8744HL8B5&keywords=fire+tv+stick&qid=1578829604&sprefix=fire%2Caps%2C709&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'} 

def send_an_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login('abc@gmail.com', 'ukxnpormfsqrcaxb')
        FROM = 'abc@gmail.com'
        TO = 'xyz@gmail.com'
        SUBJECT = "Sale on Amazon FireTVStick!"
        DESCRIPTION = 'Follow the link https://www.amazon.in/Amazon-FireTVStick-Alexa-Voice-Remote-Streaming-Player/dp/B0791YHVMK/ref=sr_1_1?crid=35GK8744HL8B5&keywords=fire+tv+stick&qid=1578829604&sprefix=fire%2Caps%2C709&sr=8-1'

        msg = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, DESCRIPTION)
        server.sendmail(FROM, TO , msg)
        print ("Mail Sent!")
        server.quit()
    except: 
        print ("Failed to send mail!")

def check_rate():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id = 'priceblock_ourprice').get_text()
    new_price = float(price[2:-3].replace(',',''))

    if new_price < 2900 :
        send_an_email()

if __name__ == "__main__":
    check_rate()
