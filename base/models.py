from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=80)
	ico = models.CharField(max_length=80,null=True)
	sort_id = models.IntegerField()
	theme =  models.CharField(max_length=80,default='x2')
	#add icon pic here
	#parent = models.ForeignKey('Category',null=True,blank=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	summary = models.CharField(max_length=250)
	description = models.TextField()
	user = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	category = models.ForeignKey('Category',null=True,blank=True)
	deleted = models.BooleanField(default=False)
	rating	= models.ForeignKey('Rating',null=True,blank=True)

	def __str__(self):
		return self.summary

class Answer(models.Model):
	description	= models.TextField()
	user = models.ForeignKey(User)
	question = models.ForeignKey('Question')
	feedback = models.ForeignKey('Feedback')
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.description

class Rating(models.Model):
	ico_name = models.CharField(max_length=80)
	value = models.IntegerField()

	def __str__(self):
		return self.ico_name

class Feedback(models.Model):
	rating = models.ForeignKey('Rating')
	created_date = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('Category')
	user = models.ForeignKey(User)

class Transport(models.Model):
	date = models.DateTimeField()
	type = models.IntegerField()
	description = models.CharField(max_length=150)
	feedback = models.ForeignKey('Feedback')

class Cafeteria(models.Model):
	date = models.DateTimeField()
	vendor = models.ForeignKey('Vendor')
	feedback = models.ForeignKey('Feedback')	

class Location(models.Model):
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

class Vendor(models.Model):
	name = models.CharField(max_length=150)
	location = models.ForeignKey('Location')
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
