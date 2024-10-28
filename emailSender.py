import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print(f'Email sent to {recipient_email}')
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {str(e)}")
        return False

def create_message(first_name, week_number, instructor_name, instructor_phone):
    return f"""Hey {first_name}, 

I hope you're doing well! We've noticed you're currently at {week_number}, and we just wanted to check in. Are you facing any challenges that are holding you back from moving forward? If so, no worries—we're here to support you every step of the way.

To help you stay on track, we'd love to have you join our WhatsApp group where you can connect with other learners: https://docs.google.com/forms/d/e/1FAIpQLScgFM4jR1sI-OD2kH-JsNPOZtOE2-7hVsgILF7alHACSJFhCw/viewform?pli=1. And if you prefer, you can also reach out to me directly on WhatsApp at {instructor_phone}. 

Looking forward to helping you succeed!

Best regards,  
{instructor_name}
"""

def send_bulk_emails(csv_file, sender_email, sender_password, subject):
    instructor_name = os.getenv('INSTRUCTOR_NAME')
    instructor_phone = os.getenv('INSTRUCTOR_PHONE')
    
    data = load_data(csv_file)

    for index, row in data.iterrows():
        first_name = row['First Name']
        week_number = row['Week']
        recipient_email = row['Email']

        body = create_message(first_name, week_number, instructor_name, instructor_phone)

        if send_email(sender_email, sender_password, recipient_email, subject, body):
            data = data.drop(index)

    data.to_csv(csv_file, index=False)
    print(f"Updated CSV saved, remaining emails: {len(data)}")

    confirmation_subject = "Email Campaign Complete"
    confirmation_body = "All emails have been sent successfully. Check the updated CSV file for details."
    send_email(sender_email, sender_password, sender_email, confirmation_subject, confirmation_body)

if __name__ == "__main__":
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('PASSWORD')
    
    csv_file = 'emails.csv'
    
    subject = "PLP Reachout"
    
    send_bulk_emails(csv_file, sender_email, sender_password, subject)
