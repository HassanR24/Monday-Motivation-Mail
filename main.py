import smtplib
import datetime as dt
from random import randint, choice

my_email = ""       #type in your email address
my_password = ""    #type in your password
receiver_email = "" #receiver's email

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as data_file:
    data = data_file.readlines()

random_quote = choice(data)

message = f"Subject:Monday Motivation\n\n{random_quote.strip()}"

if day_of_week == 3:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        #change the host and port above according to your email provider (Search google)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=message
        )
