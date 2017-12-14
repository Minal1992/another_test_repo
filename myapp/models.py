# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
	created_by = models.ForeignKey(User)
	projet_name = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):
		return self.projet_name

