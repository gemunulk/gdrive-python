from __future__ import print_function
import httplib2
import os
import io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from apiclient.http import MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Drive API Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    folder_id = input('Gdrive folder_id:')

    """
    Creates a Google Drive API service object and outputs the names and IDs of given filder id
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v3', http=http)

    results = drive_service.files().list(q="'{0}' in parents".format(folder_id) ,fields="nextPageToken, files(id, name)").execute()
    items   = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Exporting Gsheets to Excel...')
        for item in items:
            #print('{0} ({1})'.format(item['name'], item['id']))
            file_id = item['id']
            filename = item['name']
         
            MIMETYPE='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            data = drive_service.files().export(fileId=file_id, mimeType=MIMETYPE).execute()
            if data:
                fn = '%s.xlsx' % os.path.splitext(filename)[0]
                with open(fn, 'wb') as fh:
                    fh.write(data)
                print('Downloaded "%s"' % (fn))
        print('Downloaded to '+os.getcwd())

if __name__ == '__main__':
    main()


