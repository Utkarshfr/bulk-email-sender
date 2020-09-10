## A python Tkinter program to send bulk emails using gmail API

This is a easy python tkinter GUI application to send bulk emails using Gmail API.

* To get started:
1. Go to https://console.developers.google.com/ and enable the Gmail API
2. Create OAuth Client ID credentials and download it
3. Copy the credentials file to the project directory and rename it to creadentials
4. First try to send email will open browser and ask for username and password to verify the app to send emails on your behalf
5. After confirming it will download a tocken.pickle file to the project directory
6. Now you can send the Email

-
* To send bulk email you can use .csv or .xlsx files with column name as **emails** or for a single email send provide address in the to TextField
-
* The token gets expired after some time, When trying to send email the token might get refreshed before that
