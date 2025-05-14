import datetime
import smtplib

today = datetime.datetime.now()
day = today.weekday()

# day contains the index of day of the week considering monday is 0
if day == 0:

    with open("quotes.txt", "r", encoding="utf-8") as file:

        quotes = file.readlines()
        print(len(quotes))


