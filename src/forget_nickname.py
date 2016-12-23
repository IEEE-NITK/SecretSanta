import csv
import smtplib
from email.mime.text import MIMEText

hash_name = {}
hash_email = {}

with open('Secret_Santa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        name = row[1]
        nickname = row[2]
        email = row[3]
        hash_name[name] = nickname
        hash_email[name] = email 
    
    print hash_name

who = raw_input('What is your name?\n->')

#Mail written from here!
title = 'Secret Santa'
msg_content = 'Hi this is a message to remind you about Secret Santa\n' + hash_name[who]
message = MIMEText(msg_content, 'html')

message['From'] = 'Sender <santa@ieee>'
message['To'] = 'Receiver <nitk@ieee>'
message['Subject'] = 'Secret Santa'

msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('sendermail@gmail.com', 'sender_password')
server.sendmail('sendermail@gmail.com',
                [ hash_email[who] , 'salman.badshah@gmail.com'],
                msg_full)
server.quit()