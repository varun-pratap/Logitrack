# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import User
from django.db import models



# Create your models here.
class UserProfile(models.Model):
	DEPARTMENT = (
		('IT','Information Technology'),
		('Support','Support'),
		('OPPS','Operations'),
	)
	ROLES= (
		('1','MANAGER'),
		('2','SUPER USER'),
		('3','ADMIN'),
		('4','HUB INCHARGE'),
		('5','DC INCHARGE'),
		('6','Executives'),
		('7','Leads'),
	)
	user = models.OneToOneField(User)
	fname = models.CharField(max_length="20")
	lname = models.CharField(max_length="20")
	email = models.EmailField()
	employeeID = models.CharField(max_length="10")
	department = models.CharField(max_length="5",choices = DEPARTMENT)
	doj = models.DateField(auto_now = True)
	status = models.IntegerField()
	role = models.CharField(max_length="15",choices = ROLES)
