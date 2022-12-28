import smtplib
import datetime as dt
import random

MY_EMAIL = "priyanshudixit404@gmail.com"
MY_PASSWORD = "jygquefjolxlhjwd"

# now = dt.datetime.now()
# year = now.year

# if (year == 2022):
#     print("No need to wear a mask.")

# weekday = now.weekday()

# print(weekday)

# date_of_birth = dt.datetime(year= 2000, month= 10, day= 29, hour= 11, minute= 57, second= 32)

# print(date_of_birth)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("Day 32 - Birthday Wisher/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD,)
        connection.sendmail(from_addr= MY_EMAIL, 
            to_addrs= "dixitpriyanshu@yahoo.com", 
            msg= f"Subject: Daily Motivation\n\n{quote}"
            )
     