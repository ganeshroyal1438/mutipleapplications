from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return render(request,'msd.html')

def css(request):
    return HttpResponse('<h1>css is used to apply styles for html layouts')