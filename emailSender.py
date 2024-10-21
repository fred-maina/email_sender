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
    return emails

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
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {str(e)}")

# Main function to send emails to each recipient and a final confirmation email
def send_bulk_emails(csv_file, sender_email, sender_password, subject, body):
    emails = load_emails(csv_file)

    # Sending email to each recipient one by one
    for email in emails:
        send_email(sender_email, sender_password, email, subject, body)
        #time.sleep(5)  # Delay between emails to avoid overloading server

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
    subject = "PLP Reachout"
    body = """Hey, there August Cohort Learner! 👋

I'm Fredrick Maina from PLP,
Just checking in to see if you've been joining our live training sessions. We’d love to hear from you!

Could you let us know if you've been attending?
1. Yes!
2. No, not yet.
3. Not all sessions.

Also, if you're facing any issues or challenges, feel free to share them with us. We’re here to help! 😊

Looking forward to your reply!
Fredrick Maina
PLP Team"""

    # Send emails and notify after completion
    send_bulk_emails(csv_file, sender_email, sender_password, subject, body)
