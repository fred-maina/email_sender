# Email Sender Script

## Description

This Python script automates the process of sending bulk emails to a list of recipients stored in a CSV file. It allows you to send personalized emails, track which emails were successfully sent, and remove them from the CSV file. A final confirmation email is also sent once all emails are successfully delivered.

## Features

- Send personalized emails to a list of recipients.
- Remove successfully sent emails from the CSV.
- Send a final confirmation email after all emails are sent.
- Send a separate confirmation email to the administrator.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

## Setup

### Step 1: Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Linux/macOS
env\Scripts\activate     # On Windows
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 2: Create the `.env` File

In the project directory, create a `.env` file and add the following environment variables:

```
EMAIL=your-email@gmail.com
PASSWORD=your-email-password
FINAL_RECIPIENT=final-recipient-email@example.com
CONFIRMATION_RECIPIENT=confirmation-email@example.com
```

### Step 3: Prepare the CSV File

Ensure that you have a CSV file named `emails.csv` in the same directory as the script. The CSV file must have the following structure:

```
email
recipient1@example.com
recipient2@example.com
recipient3@example.com
```

Each email should be listed under the `email` column, with no other columns or extra spaces.

### Step 4: Run the Script

After setting up the `.env` file and CSV, run the script:

```bash
python emailSender.py
```

The script will:

1. Send emails to all recipients listed in the CSV file.
2. Remove the successfully sent email addresses from the CSV.
3. Send a final confirmation email to the administrator.

## Sample `.env` File

```
EMAIL=your-email@gmail.com
PASSWORD=your-email-password
FINAL_RECIPIENT=final-recipient-email@example.com
CONFIRMATION_RECIPIENT=confirmation-email@example.com
```

## Sample `emails.csv` File Format

The CSV file must have the following structure:

```
email
recipient1@example.com
recipient2@example.com
recipient3@example.com
```

- The `email` column should contain the email addresses of the recipients.
- There should be no other columns or extraneous data.

## Notes

- Make sure you have a stable internet connection for sending emails.
- If using Gmail, you need to enable "less secure apps" or generate an "App Password" for the script to work properly.
