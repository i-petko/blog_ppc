#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible
class Author(models.Model):

	author = models.CharField(max_length=20)
	email = models.EmailField()

	def __str__(self):
		return self.author


@python_2_unicode_compatible
class BlogPost(models.Model):

	name = models.CharField(max_length=160)
	text = models.TextField()
	published = models.DateTimeField(default=timezone.now)
	photo = models.ImageField(upload_to='img', blank=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.name