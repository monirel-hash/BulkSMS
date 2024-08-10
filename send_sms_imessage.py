#!/usr/bin/env python3
# Author: RealMunir
# GitHub: https://github.com/monirel-hash

import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


# Setup Google Sheets API
def setup_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client.open("BulkSMS").sheet1

# Function to send SMS
def send_sms(phone_number, message):
    script_path = 'scripts/sendiMessage.scpt'
    # Convert phone number to string
    phone_number = str(phone_number)
    message = str(message)  # Ensure message is also a string
    command = ['osascript', script_path, phone_number, message]

    print(f"Script path: {script_path}")
    print(f"Phone number: {phone_number}")
    print(f"Message: {message}")
    print(f"Command: {command}")

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error sending message: {result.stderr}")
        else:
            print(f"Message sent successfully: {result.stdout}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main function
def main():
    sheet = setup_google_sheets()
    rows = sheet.get_all_records()

    for row in rows:
        phone_number = row.get("Phone Number")
        first_name = row.get("First Name", "")
        message = row.get("Message", "Hello")
        personalized_message = f"Hello {first_name}, {message}" if first_name else message
        print(f"Sending '{personalized_message}' to {phone_number}...")
        send_sms(phone_number, personalized_message)
        time.sleep(1)  # Adjust delay as needed

if __name__ == "__main__":
    main()
