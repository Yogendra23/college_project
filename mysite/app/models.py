from django.db import models

# Create your models here.

class admin_data(models.Model):
	book_id=models.IntegerField(primary_key=True)
	book_title=models.CharField(max_length=250)
	book_image=models.ImageField(upload_to='book_images/')
	Author_name=models.CharField(max_length=100)
	price=models.IntegerField()


class user(models.Model):
	full_name=models.CharField(max_length=100)
	email_id=models.EmailField(primary_key=True)
	phone_no=models.IntegerField()
	address=models.CharField(max_length=250)
	password=models.CharField(max_length=15)
