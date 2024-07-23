# ##################### Hard Starting Project ######################
# import pandas
# import datetime as dt
# import random
# import smtplib
#
# now = dt.datetime.now()
# today = (now.month, now.day)
# print(today)
# df = pandas.read_csv("birthdays.csv")
#
# birth_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}
# # print(birth_dict)
# birthday_person = birth_dict[today]
# if today in birth_dict:
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter:
#         content = letter.read()
#         content = content.replace("[NAME]", birthday_person["name"])
#
#         my_mail = "thisisfortest8983@gmail.com"
#         with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
#             password = "put your own password"
#             # connection.starttls()
#             connection.login(user=my_mail, password=password)
#             connection.sendmail(from_addr=my_mail,
#                                 to_addrs=birthday_person["email"], msg=f"Subject:Birthday Wishes\n\n {content}")
#
#
#
#

import requests
import datetime as dt
import smtplib
import time

MY_LAT = 6.595680
MY_LONG = 3.337030

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])

    iss_positions = (iss_latitude, iss_latitude)
    #  you position +5 or -5
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    timestamp = dt.datetime.now().hour

    if timestamp >= sunset or timestamp <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        my_mail = "thisisfortest8983@gmail.com"
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            password = ""
            # connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs="pytestingtest@yahoo.com", msg="Subject:ISS\n\n look Up!!!")


