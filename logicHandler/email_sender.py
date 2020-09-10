from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
import sys


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
service = None

def main():
    global service
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)


    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        
        return False

    service = build('gmail', 'v1', credentials=creds)

    return True


def create_message(to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['subject'] = subject
  message_bytes = base64.urlsafe_b64encode(message.as_bytes())
  message_string = message_bytes.decode()
  return {'raw':message_string}


def send_message(message):
  try:
    message = (service.users().messages().send(userId='me', body=message).execute())
    return "Mail sent"

  except Exception as e:
    return f"{e}"

