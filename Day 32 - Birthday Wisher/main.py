import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "priyanshudixit404@gmail.com"
MY_PASSWORD = "jygquefjolxlhjwd"

today = dt.datetime.now()
df = pandas.read_csv("Day 32 - Birthday Wisher/birthdays.csv")
data = df.to_dict(orient="records")

letters = ["Day 32 - Birthday Wisher/letter_templates/letter_1.txt",
            "Day 32 - Birthday Wisher/letter_templates/letter_2.txt",
            "Day 32 - Birthday Wisher/letter_templates/letter_3.txt"
        ] 

for person in data:
    if today.month == person["month"] and today.day == person["day"]:
        letter_path = random.choice(letters)

        with open(letter_path) as letter:
            letter_content = letter.read()

        updated_letter = letter_content.replace("[NAME]", person["name"])
        print(updated_letter)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= person["email"],
                msg= f"Subject: Happy Birthday\n\n{updated_letter}"
            )





