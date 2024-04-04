from datetime import datetime
import random
import pandas as pd
import smtplib

my_email = "patricag912@gmail.com"
password = "ocovlxxjggeuanyh"


today = datetime.now()
today_tuple = (today.month, today.day)


data = pd.read_csv("birthdays.csv")

# Note to self for dictionary comprehension
# Format: new_key: value_expression for item in iterable
# or
# new_key, new_key: data_row for (column, data_row) in data.iterrows()
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


# Logic for sending the email.
# Checking to see if the day_month is in the csv file
if today_tuple in birthday_dict:
    # Making a variable called birthday_name that takes the whole line from the csv (name, email, year, month, day)
    birthday_name = birthday_dict[today_tuple]
    # Makes a file path that will be randomly assigned 1-3 to pick a letter.
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # Opening the file path as letter_file
    with open(file_path) as letter_file:
        # Reading the file and replacing [NAME] with the birthday person's name.
        contents = letter_file.read()
        personalized_letter = contents.replace("[NAME]", birthday_name["name"])

# Sending the letter to the person's address.
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_name["email"],
            msg=f"Subject: Happy Birthday \n\n {personalized_letter}")
