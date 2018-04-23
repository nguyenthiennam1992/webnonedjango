from django.shortcuts import render, HttpResponse
import urllib.request
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
# Create your views here.
def home(request):
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        
    return render(request,'homepage/index.html',{'files':file_list})
