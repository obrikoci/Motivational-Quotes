# SENDING A MOTIVATIONAL QUOTE
import datetime as dt
import smtplib
import random

my_email = "example@gmail.com"
password = "randompassword"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="example@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
