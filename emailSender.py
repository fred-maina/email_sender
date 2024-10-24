import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load emails from CSV
def load_emails(csv_file):
    data = pd.read_csv(csv_file)
    emails = data['email'].tolist()
    return data, emails

# Send an email using SMTP
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # SMTP server configuration
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

# Main function to send emails to each recipient and a final confirmation email
def send_bulk_emails(csv_file, sender_email, sender_password, subject, body):
    data, emails = load_emails(csv_file)

    # Sending email to each recipient one by one
    for email in emails:
        if send_email(sender_email, sender_password, email, subject, body):
            # If the email was successfully sent, remove it from the CSV data
            data = data[data['email'] != email]

    # Save the updated CSV without the sent emails
    data.to_csv(csv_file, index=False)
    print(f"Updated CSV saved, remaining emails: {len(data)}")

    # Send final email to the final recipient
    final_recipient = os.getenv('FINAL_RECIPIENT')
    send_email(sender_email, sender_password, final_recipient, "All emails sent", "All emails have been sent successfully.")

    # Send confirmation email to the confirmation recipient
    confirmation_recipient = os.getenv('CONFIRMATION_RECIPIENT')
    send_email(sender_email, sender_password, confirmation_recipient, "Emails Sent", "All emails sent, check them now.")

if __name__ == "__main__":
    # Load email and password from environment variables
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('PASSWORD')
    
    # CSV file containing emails
    csv_file = 'emails.csv'
    
    # Email content
    subject = "INSERT SUBJECT HERE"
    body = "INSERT BODY HERE"

    # Send emails and notify after completion
    send_bulk_emails(csv_file, sender_email, sender_password, subject, body)
