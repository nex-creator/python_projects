import smtplib
import random
import datetime as dt
MY_EMAIL = "zzzzzzzzzzzz@gmail.com"
PASSWORD = "zzzzzz"


now = dt.datetime.now()
day_of_week = now.weekday() #todays weekday
if day_of_week == 4:
    with open("quotes.txt","r") as data:
        all_quote = data.readlines()
        quote = random.choice(all_quote).strip()
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL, to_addrs= MY_EMAIL,
                            msg = f"Subject : quotes of the day. \n\n{quote} ")


