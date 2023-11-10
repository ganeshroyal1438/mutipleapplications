from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def pspk(request):
    return render(request,'pspk.html')

def header(request):
    return HttpResponse('<marque><h1>header are used to give titels</h1></marque>')