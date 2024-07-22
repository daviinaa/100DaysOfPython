##################### Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)
print(today)
df = pandas.read_csv("birthdays.csv")

birth_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}
# print(birth_dict)
birthday_person = birth_dict[today]
if today in birth_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])

        my_mail = "thisisfortest8983@gmail.com"
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            password = "put your own password"
            # connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=birthday_person["email"], msg=f"Subject:Birthday Wishes\n\n {content}")




