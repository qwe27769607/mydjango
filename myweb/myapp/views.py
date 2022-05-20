from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hi(request):
    return HttpResponse('<p>13232252222222222222222222222222222223</p>')
# Create your views here.
def main(request,username):
    return HttpResponse('<h1>sayhello</h1>'+username)
def main(request,username):
    now=datetime.now()
    return render(request,'hello3.html',{'username':username, 'now':now})