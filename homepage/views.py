from django.shortcuts import render, HttpResponse
import urllib.request
import backen.googledrive
# Create your views here.
def home(request):
    backen.googledrive.upload_file(backen.googledrive.get_drive())
    return render(request,'homepage/index.html',{'files':'list_id'})
