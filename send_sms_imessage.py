#!/usr/bin/env python3

import os
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess

# Setup Google Sheets API
def setup_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client.open("BulkSMS").sheet1

# Function to send SMS
def send_sms(phone_number, message):
    script_path = 'scripts/sendiMessage.scpt'
    command = ['osascript', script_path, phone_number, message]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error sending message: {result.stderr}")

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
