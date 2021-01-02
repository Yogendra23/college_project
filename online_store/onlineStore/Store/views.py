from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse



def index(request):
	return render(request,'index.html',{'site':site})

def shop(request):
	return render(request,'shop.html')

def about(request):
	return render(request,'about.html')

def product_details(request):
	return render(request,'product_details.html')

def blog(request):
	return render(request,'blog.html')

def blog_details(request):
	return render(request,'blog_details.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST.get('name')
		email =  request.POST.get('email')
		password =  request.POST.get('password')
		if not User.objects.filter(email=email).exists(): 
			User(username=username,email=email,password=password).save()
		else:
			return HttpResponse('This email already exists.')
		return HttpResponseRedirect('/login/')
	else:
		return render(request, 'signup.html')

def login(request):
	return render(request,'login.html')

def cart(request):
	return render(request,'cart.html')

def elements(request):
	return render(request,'elements.html')

def confirmation(request):
	return render(request,'confirmation.html')

def checkout(request):
	return render(request,'checkout.html')


def contact(request):
	return render(request,'contact.html')