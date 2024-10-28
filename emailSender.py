import smtplib
import pandas as pd
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def load_data(csv_file):
    return pd.read_csv(csv_file)

def load_resources(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

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

def create_message(first_name, week_number, resources, instructor_name, instructor_phone):
    # Get the appropriate resources for the given week
    week_key = week_number.strip()  # Ensure there are no extra spaces
    recordings_link = resources.get(week_key, {}).get("recordings_link", "N/A")
    assignment_link = resources.get(week_key, {}).get("assignment_link", "N/A")
    dataset_link = resources.get(week_key, {}).get("assignment_dataset", None)
    
    # Construct the email message with or without the dataset link
    if dataset_link:
        dataset_section = f"\n📊 {week_key} Dataset: {dataset_link}\n"
    else:
        dataset_section = ""

    return f"""🌟 Checking In on Your Database Design Journey!

Hi {first_name},

I hope you’re having a great day! 😊

I wanted to check in on your progress in {week_key} of the Database Design course. Remember, everyone learns at their own pace, and I’m here to support you!

If you're feeling stuck or have questions, don’t hesitate to reach out. I'm excited to help you succeed! 🎉

Here are some useful resources:

📹 {week_key} Recordings: {recordings_link}
📚 {week_key} Assignment: {assignment_link}{dataset_section}

Practice is key to success in this course! The more you engage with SQL, the more comfortable you’ll become.

I can’t wait to see your progress! Let’s make this an amazing learning experience! 🚀

Best regards,  
{instructor_name}  
{instructor_phone}"""

def send_bulk_emails(csv_file, json_file, sender_email, sender_password, subject):
    instructor_name = os.getenv('INSTRUCTOR_NAME')
    instructor_phone = os.getenv('INSTRUCTOR_PHONE')
    
    data = load_data(csv_file)
    resources = load_resources(json_file)

    for index, row in data.iterrows():
        first_name = row['First Name']
        week_number = row['Week']  # The value is like 'Week 1', 'Week 2', etc.
        recipient_email = row['Email']

        body = create_message(first_name, week_number, resources, instructor_name, instructor_phone)

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
    json_file = 'course_resources.json'  # Path to your JSON file containing course resources
    
    subject = "PLP Reachout"
    
    send_bulk_emails(csv_file, json_file, sender_email, sender_password, subject)
