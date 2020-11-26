from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
 return render(request, 'covid_project/login.html')