# coding: utf-8
from django.db import models


class Testimonial(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=600)
	photo = models.ImageField(upload_to='imgtestimonials')
	create_in = models.DateTimeField(auto_now_add=True, editable=False)
	modify_on = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name


class Gallery(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='imggallery')
	create_in = models.DateTimeField(auto_now_add=True, editable=False)
	modify_on = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name
