from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

def get_drive():
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance
    return drive

def upload_file(drive):
    file1 = drive.CreateFile({'title': 'testok.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentString('susseful!') # Set content of the file from given string.
    file1.Upload()
    return file1