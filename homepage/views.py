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
    auth_url = gauth.CommandLineAuth()
    return render(request,'homepage/index.html',{'CLIENT_ID':auth_url})