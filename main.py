from datetime import datetime
import pandas
import random
import smtplib
from email.message import EmailMessage

MY_EMAIL = "sahiladhi39@gmail.com"
MY_PASSWORD = "oigz jcgc mpss abwc"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Set up the email message
    msg = EmailMessage()
    msg.set_content(f'{contents}')

    msg['Subject'] = 'Subject:Happy Birthday!'
    msg['From'] = 'sahiladhi39@gmail.com'
    msg['To'] = birthday_person["email"]

    # Send the email using Gmail's SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('sahiladhi39@gmail.com', 'oigz jcgc mpss abwc')
    s.send_message(msg)
    s.quit()

