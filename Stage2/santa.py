import csv
import smtplib
from email.mime.text import MIMEText

hash1 = {}
hash2 = {}
hash3 = {}
nicknames = []

with open('Secret_Santa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        name = row[1]
        nickname = row[2]
        email = row[3]
        hash1[nickname] = name
        hash2[nickname] = email 
    
    print hash1

with open('Santa_Choose.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        nickname = row[1]
        chosen_nickname = row[2]
        hash3[nickname] = chosen_nickname 
        nicknames.append(nickname)

for nickname in nicknames:
    who = nickname
    whatName = hash3[nickname]

    #Mail written from here!
    title = 'Secret Santa'
    msg_content = 'Hi this is a message to tell you about your Secret Santa\n' + hash1[whatName]
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Sender Name <sender@server>'
    message['To'] = 'Receiver Name <receiver@server>'
    message['Cc'] = 'Receiver2 Name <receiver2@server>'
    message['Subject'] = 'Secret Santa'

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('secret.santa.ieeenitk@gmail.com', 'ieeenitk2016')
    server.sendmail('secret.santa.ieeenitk@gmail.com',
                    [ hash2[who] , 'salman.badshah@gmail.com'],
                    msg_full)
    server.quit()