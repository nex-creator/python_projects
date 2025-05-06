##################### Extra Hard Starting Project ######################
import pandas as pd
from datetime import datetime
import random
import smtplib
MY_EMAIL = "ppoksja@gmail.com"
PASSWORD = "zzzzzzzzzz"
PLACEHOLDER = "[Name]"

# 2. Check if today matches a birthday in the birthdays.csv
today = (datetime.now().month, datetime.now().day)

data = pd.read_csv("birthdays.csv")
birthday_dict ={(data_row.month,data_row.day): data_row for(index,data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person =birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER,birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject : BirthdayWish. \n\n{contents} ")




