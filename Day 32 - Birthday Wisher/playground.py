import smtplib
from email.mime.text import MIMEText

# Set up the SMTP server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("priyanshudixit404@gmail.com", "jygquefjolxlhjwd")

# Construct the email message
msg = MIMEText("This is the body of the email")
msg['To'] = "dixitpriyanshu@yahoo.com"
msg['Subject'] = "Test Email"

# Send the email
server.send_message(msg)

# Disconnect from the server
server.quit()
