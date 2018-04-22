from django.shortcuts import render, HttpResponse
import urllib.request
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
# Create your views here.
def home(request):
    
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false and mimeType='video/mp4'" % '1cJ0vNiEq2bo_Ui5r2qIfdhASeNTNjCc-'}).GetList()
    return render(request,'homepage/index.html',{'contents':file_list})