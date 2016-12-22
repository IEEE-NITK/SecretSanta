import smtplib
from email.mime.text import MIMEText

title = 'Secret Santa'
msg_content = 'Hi this is a message to tell you about your Secret Santa\n'.format(title=title)
message = MIMEText(msg_content, 'html')

message['From'] = 'Sender Name <sender@server>'
message['To'] = 'Receiver Name <receiver@server>'
message['Cc'] = 'Receiver2 Name <receiver2@server>'
message['Subject'] = 'Secret Santa'

msg_full = message.as_string()

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('sendermail@gmail.com', 'sender_password')
server.sendmail('sendermail@gmail.com',
                ['recievermail1@gmail.com', 'recievermail2@gmail.com'],
                msg_full)
server.quit()