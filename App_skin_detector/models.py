from django.db import models
from django.db.models import Model


# Create your models here.om django.db.models import Model
class loggedin(models.Model):
	name=models.CharField(max_length=100,default=None)
	email=models.CharField(max_length=100,default=None)
	username=models.CharField(max_length=100,default=None)
	password=models.CharField(max_length=10,default=None)
	confirm_password=models.CharField(max_length=100,default=None)

class AdminDetails(models.Model):
	username = models.CharField(max_length=100,default=None,null=True)
	password = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'AdminDetails'

class Feedback_details(models.Model):
	firstname = models.CharField(max_length=100,default=None,null=True)
	lastname = models.CharField(max_length=100,default=None,null=True)
	mailid = models.CharField(max_length=100,default=None,null=True)
	feedback = models.CharField(max_length=200,default=None,null=True)
	class Meta:
		db_table = 'Feedback_details'

class Doctor_detail(models.Model):
	name 	= models.CharField(max_length=100,null=True,default=None)
	Gender = models.CharField(max_length=100,null=True,default=None)
	Speciality 	= models.CharField(max_length=100,null=True,default=None)
	Department 	= models.CharField(max_length=100,null=True,default=None)
	class Meta:
		db_table = 'Doctor_detail'

class medicine_detail(models.Model):
	medicine_name = models.CharField(max_length=100,null=True,default=None)
	medicine_on   = models.CharField(max_length=100,null=True,default=None)
	medicine_type = models.CharField(max_length=100,null=True,default=None)
	description   = models.CharField(max_length=100,null=True,default=None)
	price 		  = models.CharField(max_length=100,null=True,default=None)
	class Meta:
		db_table = 'medicine_detail'
