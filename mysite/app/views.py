from django.shortcuts import render,redirect
from app.models import admin_data,user
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def mainfunc(request):
	return render(request,'index.html')

def bookspage(request):
	book_info=admin_data.objects.all()
	return render(request,'book_page.html',{'book_info':book_info})

def register(request):
	return render(request,'register.html')

def login(request):
	book_id=request.POST.get('x1')
	full_name=request.POST.get('u1')
	email_id=request.POST.get('u2')
	phone_no=request.POST.get('u3')
	password=request.POST.get('u4')
	address=request.POST.get('u5')
	try:
		user_data=user(full_name=full_name,email_id=email_id,phone_no=phone_no,password=password,address=address)
		user_data.save()
		return render(request,'login.html',{'book_id':book_id})
	except IntegrityError:
		return render(request,'login.html',{'book_id':book_id})
	
def next(request):
	book_id=request.POST.get('z1')
	email_id=request.POST.get('l1')
	password=request.POST.get('l2')
	try:
		data=user.objects.get(email_id=email_id,password=password)
		if data.email_id==email_id and data.password==password:
			if book_id:
				book_info=admin_data.objects.get(book_id=book_id)
				user_info=user.objects.get(email_id=email_id)
				return render(request,'thankyou.html',{'book_info':book_info,'user_info':user_info})
			else:
				response=redirect('/bookspage/')
				return response
		else:
			return render(request,'login.html',{'error':'Please enter a valid Email and Password!!!'})
	except ObjectDoesNotExist:
		return render(request,'login.html',{'error':'Please enter a valid Email and Password!!!'})

