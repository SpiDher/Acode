import smtplib,csv
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from random import randint
from threading import Timer
from csv import DictReader
import sys


generator = lambda length:''.join(str(randint(0,9)) for _ in range(length))
OTP = None
def OTP_counter(seconds):
    global OTP
    OTP = generator(4)  # Generate the OTP here
    Timer(int(seconds), lambda: None).start()  # You can adjust this if you want to handle OTP expiration
    return OTP

def smtp_login():
    with open('login.csv','r') as file:
        reader = DictReader(file)
        for param in reader:
            return (param['email'], param['password'])

def get_emails():
    emails =[]
    with open('email_list.csv', 'r') as file:
        email_list = csv.reader(file)
        for email in email_list:
            emails.append(email[0])
    return emails

def send_email(send_to,send_from,text,subject):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    try:
        smtp = smtplib.SMTP('smtp.gmail.com: 587')
        smtp.starttls()
        smtp.login(*smtp_login())
        smtp.sendmail(send_from,send_to,msg.as_string())
        
    except Exception as e:
        print(f'failed to send email {str(e)}')

def confirm_otp():
    try:
        user_otp = str(input('Enter OTP send to your email: '))
        if user_otp == OTP:
            print('OTP confirmed')
        else:
            print('Invalid OTP')
    except Exception as e:
        print(e)
    
def main():
    OTP_counter(120)
    emails = get_emails()
    for email in emails:
        send_email(send_to=email, send_from=smtp_login()[0], text=OTP, subject='Test OTP')
    print('OTP sent to emails provided at email_list.csv')
    confirm_otp()
    sys.exit()
if __name__ == '__main__':
    main()