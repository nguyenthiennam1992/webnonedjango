from django.shortcuts import render, HttpResponse
import urllib.request
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Create your views here.
def home(request):
    # Define the credentials folder
    home_dir = os.path.expanduser("~")
    credential_dir = os.path.join(home_dir, ".credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, "pydrive-credentials.json")

    # Start authentication
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile(credential_path)
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.CommandLineAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile(credential_path)

    # drive = GoogleDrive(gauth)
    # gauth = GoogleAuth()
    # gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false and mimeType='video/mp4'" % '1yYO8HfDvJNcdgLYB-Ms9v4q2VQjUFpHx'}).GetList()
    return render(request,'homepage/index.html',{'contents':file_list})