# Form Link: https://docs.google.com/forms/d/e/1FAIpQLSfHeqRPS-wCnGX2uxIaOSoPbvrmkwP13i8M5ez68KoMjvvo3A/viewform?usp=sf_link

# Import smtplib for our actual email sending function
import smtplib

# Helper email modules
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import pandas for reading the excel file
import pandas as pd

############################ CONFIG BLOCK #################################
# sender email address
email_user = 'ieee.nitk.secretsanta@gmail.com'

# sender email passowrd for login purposes
email_password = 'YourPassword'

# Email subject
subject = "Your IEEE Secret Santa's Information!"

# Excel file name
file_name = "secretsanta.xlsx"

# Excel sheet name
sheet_name = "Sheet3"

############################ CONFIG ENDS ##################################

# Setup the email server
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

# Read the excel file
df = pd.read_excel(file_name, sheet_name=sheet_name)

for _, row in df.iterrows():
    # Get the email address of the recipient
    email_send = row["Emails"]
    print("Sending email to", email_send, "...")

    # Fill in details of the email
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # Email body in HTML
    body = f"""<html>
                <head>
                    <style>
                        table, th, td {{
                            border: 1px solid black;
                            border-collapse: collapse;
                        }}
                    </style>
                </head>
                <body>
                <h1>Hello {row['From']}, Greetings from IEEE NITK!</h1>
                <p>Your Secret Santa information is here (at long last!). We had to configure a fancy script that sent out all the emails at once to the right people with the right information. <s>Hopefully</s> the info you have is correct. Merry Christmas, and Happy Holidays!</p>
                <p>Couple of Guidelines regarding the gifting:</p>
                <ul>
                    <li>Gifts should be of a value of <b>₹500</b> or less.</li>
                    <li>You can use the information below to choose a nice, relevant gift.</li>
                    <li>You cannot interact with your <i>giftee</i>.</li>
                    <li>Gifts will be exchanged offline tentatively in the <b>second week of January</b>.</li>
                    <li>Most other <a href="https://www.elfster.com/content/secret-santa-rules/">Secret Santa rules</a> apply.</li>
                </ul>
                <p>Here's your Secret Santa's information:</p>
                <table>
                    <thead>
                        <tr>
                            <th>Field</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Name</td>
                            <td>{row['Name']}</td>
                        </tr>
                        <tr>
                            <td>Phone Number</td>
                            <td>{row['Phone Number']}</td>
                        </tr>
                        <tr>
                            <td>Email Address</td>
                            <td>{row['To']}</td>
                        </tr>
                        <tr>
                            <td>Top 3 favorite series/movies/bands</td>
                            <td>{row['Q1']}</td>
                        </tr>
                        <tr>
                            <td>List three things you dislike as a gift</td>
                            <td>{row['Q2']}</td>
                        </tr>
                        <tr>
                            <td>On a rainy Saturday, you:</td>
                            <td>{row['Q3']}</td>
                        </tr>
                        <tr>
                            <td>What activity do you prefer?</td>
                            <td>{row['Q4']}</td>
                        </tr>
                        <tr>
                            <td>On your trip to somewhere away in the mountains, what would you like to take with you?</td>
                            <td>{row['Q5']}</td>
                        </tr>
                        <tr>
                            <td>Which color scheme attracts you the most?</td>
                            <td>{row['Q6']}</td>
                        </tr>
                        <tr>
                            <td>What kind of fit do you prefer?</td>
                            <td>{row['Q7']}</td>
                        </tr>
                        <tr>
                            <td>What is the one thing you wish you had in your hostel room?</td>
                            <td>{row['Q8']}</td>
                        </tr>
                        <tr>
                            <td>If not engineering, what else would you choose?</td>
                            <td>{row['Q9']}</td>
                        </tr>
                        <tr>
                            <td>Anything else you'd like to add to help the Secret Santa choose a gift for you?</td>
                            <td>{row['Q10']}</td>
                        </tr>
                    </tbody>
                </table>
                <p>Thank you for participating in the IEEE NITK Secret Santa 2022! We hope you have a great time with your Secret Santa!</p>
                <p>Regards,</p>
                <p>IEEE NITK</p>
                <p>PS: If there's a 0 in a field, it's most likely an empty field xD. For any queries, contact <a href="https://wa.me/919481434312">Anannya</a> or <a href="https://wa.me/918867907525">Nishant</a>. Or reply to this email :P</p>
                </body>
            </html>
        """

    # Attach the body to the email
    msg.attach(MIMEText(body, 'html'))

    # Convert the email to a string
    text = msg.as_string()

    # Send the email
    server.sendmail(email_user, email_send, text)
    print("Email sent to", email_send, "successfully! 🎉")

server.quit()
