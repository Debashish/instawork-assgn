# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Team(models.Model):

	memberid = models.CharField(max_length=100, unique=True)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	phonenumber = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	role = models.CharField(max_length=100)

	class Meta:
		db_table = 'teamdata'
