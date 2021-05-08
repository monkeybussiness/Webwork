from django.shortcuts import render


# Create your views here.

def index(requests):
	return render(requests, 'app/index.html')

def register(requests):
	return render(requests, 'app/register.html')

def login(requests):
	return render(requests, 'app/login.html')
