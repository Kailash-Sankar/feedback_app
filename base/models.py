from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=80)
	sort_id = models.IntegerField()
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

	def __str__(self):
		return self.summary

class Answer(models.Model):
	description	= models.TextField()
	user = models.ForeignKey(User)
	question = models.ForeignKey('Question')
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.description
