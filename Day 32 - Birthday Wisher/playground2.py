import smtplib

my_email = "priyanshudixit404@gmail.com"
my_password = "jygquefjolxlhjwd"

connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)

connection.login(my_email, my_password,)
connection.sendmail(from_addr= my_email, 
    to_addrs= "dixitpriyanshu@yahoo.com", 
    msg= "Subject:Happ Birthday\n\nMazaak tha bhai.\nMazaak"
    )
connection.close()
