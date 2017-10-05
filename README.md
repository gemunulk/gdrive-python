# gdrive-python

# Prerequisites
To run this scripts, you'll need followings:
- [Python 3.x](https://www.python.org/downloads/)
- The pip3 package management tool.
- Access to the internet and a web browser.
- A Google account with Google Drive enabled.

## Step 1: Turn on the Drive API

- Use [this wizard] (https://console.developers.google.com/start/api?id=drive) to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
- On the Add credentials to your project page, click the Cancel button.
- At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
- Select the Credentials tab, click the Create credentials button and select OAuth client ID.
- Select the application type Other, enter the name "Drive API Quickstart", and click the Create button.
- Click OK to dismiss the resulting dialog.
- Click the file_download (Download JSON) button to the right of the client ID.
- Move this file to your working directory and rename it client_secret.json.

## Step 2: Install the Google Client Library

Run the following command to install the library using pip:
````
pip3 install --upgrade google-api-python-client
````

Ref. [Python Quickstart](https://developers.google.com/drive/v3/web/quickstart/python)

### Set up
This project requires pip to install dependencies. To install dependencies run :  
````
cd /gsheet_to_excel
pip3 install -r requirements.txt
````

### Execute script 
````
cd /gsheet_to_excel
python3 gsheet_to_excel.py 
````
