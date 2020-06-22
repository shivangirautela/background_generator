import smtplib #to create a smtp server to connect to emails
from email.message import EmailMessage
from string import Template
from pathlib import Path #same as os.Path helps to access index.html

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Shivangi Rautela'
email['to']= 'ssroutela68@gmail.com'
email['subject'] = 'you won 100000 dollars!'

email.set_content(html.substitute(name ='tintin'),'html') # name could be in dictionary type also 

with smtplib.SMTP(host ='smtp.gmail.com',port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shivangirautela22@gmail.com','@%password%@9')
    smtp.send_message(email)
    print('all good boss!')

