from django.shortcuts import render,HttpResponse
from translate import Translator
# Create your views here.
def home(request):
    return render(request, 'base.html')

def translate(request):
    return render(request, 'translate.html')

def weather(request):
    return render(request, 'weather.html')

def starplace(request):
    return render(request, 'starplace.html')

def notice(request):
    return render(request, 'notice.html')

