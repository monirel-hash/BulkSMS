# BulkSMS

Sample script for sending iMessage using Python3 and Apple Script.

Usage (MacOS with active iMessage only):

```bash
python3 send_sms_imessage.py
```

> I used Python to make it simple xD

Inspired by [Night].
# BulkSMS


## Overview
BulkSMS is a Python-based application designed to send bulk SMS messages via iMessage, integrating with Google Sheets for managing recipient data. This project allows users to automate the sending of personalized messages directly from their MacBook.

## Features
- Read phone numbers and messages from a Google Sheets document.
- Send messages via AppleScript and iMessage.
- Easy to use and integrate into your daily workflow.

## Prerequisites
Before you start using BulkSMS, make sure you have the following installed:
- Python 3.8 or higher
- A valid Google Cloud Service Account with access to Google Sheets API

## Installation

Clone the repository:
```bash
git clone https://github.com/monirel-hash/BulkSMS.git
cd BulkSMS
```

Set up a virtual environment and install the dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Configuration
Place your credentials.json for Google API in the project root.
Ensure you have set up a Google Sheet with the following columns:
Phone Number
First Name
Message (optional)
Usage
Run the script from the command line:
```
python send_sms_imessage.py
```
