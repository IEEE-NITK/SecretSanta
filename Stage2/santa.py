# n_name - Nickname
# ch_n_name - Chosen NickName

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
        nicknames.append(nickname)
    
    #print hash1


with open('Santa_Choose.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        nickname = row[1]
        chosen_nickname = row[0]
        hash3[nickname] = chosen_nickname 


for nickname in nicknames:
    #who = nickname
    #whatName = hash3[nickname]

    #Mail written from here!
    title = 'Secret Santa'
    msg_content = """
    Hey,
    This is a message from the Secret Santa Team!<br><br>
    Congratulations on being a part of IEEE-NITK Secret Santa 2k16.<br>
    """ 
    msg_content += "You are a Secret Santa for " + hash1[hash3[nickname]]
    msg_content += """
    <br>Hope to see you soon.
    <br><br>Best regards,<br>
    Secret Santa Team
    """
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Sender <santa@ieee>'
    message['To'] = 'Receiver <nitk@ieee>'
    message['Subject'] = 'Secret Santa Disclosure'

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('secret.santa.ieeenitk@gmail.com', 'ieeenitk2016')
    server.sendmail('secret.santa.ieeenitk@gmail.com',
                    [ hash2[nickname] , 'salman.badshah@gmail.com'],
                    msg_full)
    server.quit()