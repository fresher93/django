from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
	print(request)
	return HttpResponse("<html><body>Login</body></html>")
