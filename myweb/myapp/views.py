from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return HttpResponse('<p>13232252222222222222222222222222222223</p>')
# Create your views here.
def main(request):
    return HttpResponse('<h1>123213</h1>')