from django.shortcuts import render, HttpResponse
import urllib.request
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
import google.oauth2.credentials
import google_auth_oauthlib.flow
from pydrive.auth import GoogleAuth
# Create your views here.
def home(request):
    gauth = GoogleAuth()
<<<<<<< HEAD
    auth_url = gauth.CommandLineAuth()
    return render(request,'homepage/index.html',{'CLIENT_ID':auth_url})
=======
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
    return render(request,'homepage/index.html',{''})
>>>>>>> 75ccf151ce29c22ce21cba06332adc490d0f5e48
