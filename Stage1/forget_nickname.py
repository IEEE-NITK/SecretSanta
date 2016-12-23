import csv
import smtplib
from email.mime.text import MIMEText

hash_nickname = {}
hash_email = {}
names = []
nicknames = []

with open('Secret_Santa.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        #Assign values to each variable
        name = row[1]
        nickname = row[2]
        email = row[3]
        #
        hash_nickname[name] = nickname
        hash_email[name] = email 
        names.append(name)
        nicknames.append(nickname)

    print hash_nickname

with open('Santa_Choose.csv', 'w') as csvfile:
    writeCSV = csv.writer(csvfile)

    writeCSV.writerow(['Nicknames', 'Chosen Nicknames'])

    for nickname in nicknames:
        writeCSV.writerow([nickname])

for name in names:
    #Mail written from here!
    title = 'Secret Santa'
    msg_content = '''
    Hey,\n
    You are recieving this mail to confirm that you have registered for Secret Santa 2k16.\n\n 
    '''
    msg_content += 'Your nickname that you have chosen is: ' + hash_nickname[name]
    msg_content += '''
    \nLooking forward to an amazing year with you up ahead\n\n
    Best Regards,\n
    Secret Santa 2k16 Team.
    '''
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Sender <santa@ieee>'
    message['To'] = 'Receiver <nitk@ieee>'
    message['Subject'] = 'Secret Santa'

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('secret.santa.ieeenitk@gmail.com', 'ieeenitk2016')
    server.sendmail('secret.santa.ieeenitk@gmail.com',
                    [ hash_email[name] , 'salman.badshah19@gmail.com'],
                    msg_full)
    server.quit()