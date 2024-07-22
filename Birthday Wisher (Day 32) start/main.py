import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
with open("quotes.txt", "r") as file:
    quotes_list = file.readlines()

if day_of_the_week == 0:
    stripped_quote = [n.strip() for n in quotes_list]
    quote_ofthe_day = random.choice(stripped_quote)

    my_mail = "thisisfortest8983@gmail.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        password = "put your own password"
        # connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs="pytestingtest@yahoo.com", msg=f"Subject:Motivational Quotes\n\n "
                                                                                   f"{quote_ofthe_day}")
