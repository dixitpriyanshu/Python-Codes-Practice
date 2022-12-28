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
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= person["email"],
                msg= f"Subject: Happy Birthday\n\n{updated_letter}"
            )

#----------------------ALTERNATE APPROACH---------------#

# today = dt.datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
    