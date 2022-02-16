from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def toy(request):
	return HttpResponse('hello')