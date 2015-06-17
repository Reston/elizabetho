#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from elizabetho.apps.homepage.forms import contactForm, realcontactForm
from elizabetho.apps.homepage.models import Testimonial
from elizabetho.apps.gallerypath.models import Gallery, Image
from django.template import RequestContext
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def index(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()
	#llamados
	try:
		gallery = Gallery.objects.get(path=request.build_absolute_uri())
	except ObjectDoesNotExist:
		gallery = None
		llamados = None
	except MultipleObjectsReturned:
		gallery = Gallery.objects.filter(path=request.build_absolute_uri())[0]
	if gallery:
		llamados = Image.objects.filter(gallery=gallery)
	testimonials = Testimonial.objects.all()[:4]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'gallery': gallery, 'llamados': llamados}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))


def about(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()
	#llamados
	try:
		gallery = Gallery.objects.get(path=request.build_absolute_uri())
	except ObjectDoesNotExist:
		gallery = None
		llamados = None
	except MultipleObjectsReturned:
		gallery = Gallery.objects.filter(path=request.build_absolute_uri())[0]
	if gallery:
		llamados = Image.objects.filter(gallery=gallery)
	testimonials = Testimonial.objects.all()[:4]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'gallery': gallery, 'llamados': llamados}
	return render_to_response('homepage/about.html', ctx, context_instance=RequestContext(request))


def services(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = contactForm()
	#llamados
	try:
		gallery = Gallery.objects.get(path=request.build_absolute_uri())
	except ObjectDoesNotExist:
		gallery = None
		llamados = None
	except MultipleObjectsReturned:
		gallery = Gallery.objects.filter(path=request.build_absolute_uri())[0]
	if gallery:
		llamados = Image.objects.filter(gallery=gallery)
	testimonials = Testimonial.objects.all()[:4]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'gallery': gallery, 'llamados': llamados}
	return render_to_response('homepage/services.html', ctx, context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = realcontactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s mail: %s Tipo de servicio: %s Plan: %s' % (cd['nombre'], cd['email'], cd['tipoServicio'], cd['planes'])
			content = u'Email contacto: %s \nAsunto: %s \nTelefono: %s \nDescripcion: %s' % (cd['email'], asunto, cd['telefono'], cd['texto'])
			send_mail(asunto, content, cd['email'], ['info@duranjo.com'])
	else:
		form = realcontactForm()
	testimonials = Testimonial.objects.all()[:4]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials}
	return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))
