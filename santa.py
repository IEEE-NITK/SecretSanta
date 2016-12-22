import csv
import smtplib
from email.mime.text import MIMEText

with open('Secret_Santa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    hash1 = {}
    hash2 = {}
    #nicknames = []
    #names = []
    for row in readCSV:
        name = row[1]
        nickname = row[2]
        email = row[3]
        hash1[nickname] = name
        hash2[nickname] = email 
        #nicknames.append(nickname)
        #names.append(name)

    #print(nicknames)
    #print(names)

    print hash1

    whatName = raw_input('Whose name do you wish to know?\n->')
    #coldex = names.index(whatName)
    #theNickname = nicknames[coldex]
    #print('The name of ' + whatName + ' is: ' + hash1[whatName])
    #print('The email of ' + whatName + ' is ' + hash2[whatName])

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
server.login('sbs.191197@gmail.com', 'salman@nitk2015')
server.sendmail('sbs.191197@gmail.com',
                [ hash2[whatname], 'salman.badshah@gmail.com'],
                msg_full)
server.quit()