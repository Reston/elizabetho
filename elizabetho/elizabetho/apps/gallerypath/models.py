#-*- coding: utf-8
from django.db import models


class Gallery(models.Model):
	title = models.CharField(max_length=50)
	path = models.CharField(max_length=100)
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Galerias de llamados"
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.title


class Image(models.Model):
	title = models.CharField(max_length=140)
	gallery = models.ForeignKey(Gallery, related_name='Galeria')
	image = models.ImageField(upload_to='imgslider', help_text="Se recomienda usar fotos de más de 300 de ancho por al menos 300 de alto.")
	alt = models.CharField(max_length=140)
	url_to = models.CharField(max_length=140, help_text="Enlace hacia donde redireccionara el llamado")
	creado_en = models.DateTimeField(auto_now_add=True, editable=False)
	modificado_en = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title
