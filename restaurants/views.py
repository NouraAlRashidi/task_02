from django.shortcuts import render

def rest_function (request):
	context = {"msg": 'Hello World!',}
	return render (request, "menu.html" ,context) 
# Create your views here.
