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
INSTRUCTOR_NAME=Your Name
INSTRUCTOR_PHONE=+254XXXXXXXXX
```

### Step 3: Prepare the CSV File

Ensure that you have a CSV file named `emails.csv` in the same directory as the script. The CSV file must have the following structure:

```
Email,First Name,Middle Name,Last Name,Completion (%),Country,Phone Number,Gender,Academic Level,Week,Assignee,Response,Comments,Follow up date
john.doe@example.com,John,N/A,Doe,75.0,USA,+1234567890,male,UnderGraduate,Week 1,,,,,
jane.smith@example.com,Jane,N/A,Smith,85.5,UK,+0987654321,female,PostGraduate,Week 2,,,,,
sam.brown@example.com,Sam,N/A,Brown,90.0,Canada,+1122334455,male,UnderGraduate,Week 3,,,,,

```

Each email should be listed under the `Email` column along with the other relevant details.

### Step 4: Run the Script

After setting up the `.env` file and CSV, run the script:

```bash
python emailSender.py
```

The script will:

1. Send emails to all recipients listed in the `emails.csv` file.
2. Remove successfully sent email addresses from the CSV, ensuring that they are no longer part of the list for future sends.
3. Send a final confirmation email to the administrator.

## Sample `.env` File

```
EMAIL=your-email@gmail.com
PASSWORD=your-email-password
INSTRUCTOR_NAME=Your Name
INSTRUCTOR_PHONE=+254XXXXXXXXX
```

## Sample `emails.csv` File Format

The CSV file must have the following structure:

```
Email,First Name,Middle Name,Last Name,Completion (%),Country,Phone Number,Gender,Academic Level,Week,Assignee,Response,Comments,Follow up date
john.doe@example.com,John,N/A,Doe,75.0,USA,+1234567890,male,UnderGraduate,Week 1,,,,,
jane.smith@example.com,Jane,N/A,Smith,85.5,UK,+0987654321,female,PostGraduate,Week 2,,,,,
sam.brown@example.com,Sam,N/A,Brown,90.0,Canada,+1122334455,male,UnderGraduate,Week 3,,,,,

```

- The `Email` column should contain the email addresses of the recipients.
- There should be no other columns or extraneous data.

## Notes

- Make sure you have a stable internet connection for sending emails.
- If using Gmail, you need to enable "less secure apps" or generate an "App Password" for the script to work properly.
- Successfully sent emails will be deleted from the `emails.csv` file to keep the list updated.