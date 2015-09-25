#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from elizabetho.apps.homepage.forms import contactForm, realcontactForm
from elizabetho.apps.homepage.models import Testimonial, Gallery as GalleryBig
from elizabetho.apps.gallerypath.models import Gallery, Image
from django.template import RequestContext
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from zinnia.models import Entry


def index(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s Email: %s Phone: %s' % (cd['name'], cd['email'], cd['phone'])
			content = u'Name: %s \nEmail: %s \nPhone: %s \nGender: %s \nHeight: %s \nWeight: %s \nSkin Color: %s \nHair Color: %s \nProfession: %s \nHobbies: %s \nFavorite Colors: %s' % (
				cd['name'], cd['email'], cd['phone'], cd['gender'], cd['height'], cd['weight'], cd['skin_color'], cd['hair_color'], cd['profession'], cd['hobbies'], cd['favorite_colors'])
			send_mail(asunto, content, cd['email'], ['elizabeth@elizabetholive.us'])
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
	testimonials = Testimonial.objects.all()[:3]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'gallery': gallery, 'llamados': llamados}
	return render_to_response('homepage/index.html', ctx, context_instance=RequestContext(request))


def about(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s Email: %s Phone: %s' % (cd['name'], cd['email'], cd['phone'])
			content = u'Name: %s \nEmail: %s \nPhone: %s \nGender: %s \nHeight: %s \nWeight: %s \nSkin Color: %s \nHair Color: %s \nProfession: %s \nHobbies: %s \nFavorite Colors: %s' % (
				cd['name'], cd['email'], cd['phone'], cd['gender'], cd['height'], cd['weight'], cd['skin_color'], cd['hair_color'], cd['profession'], cd['hobbies'], cd['favorite_colors'])
			send_mail(asunto, content, cd['email'], ['elizabeth@elizabetholive.us'])
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
	testimonials = Testimonial.objects.all()[:6]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'gallery': gallery, 'llamados': llamados}
	return render_to_response('homepage/about.html', ctx, context_instance=RequestContext(request))


def services(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s Email: %s Phone: %s' % (cd['name'], cd['email'], cd['phone'])
			content = u'Name: %s \nEmail: %s \nPhone: %s \nGender: %s \nHeight: %s \nWeight: %s \nSkin Color: %s \nHair Color: %s \nProfession: %s \nHobbies: %s \nFavorite Colors: %s' % (
				cd['name'], cd['email'], cd['phone'], cd['gender'], cd['height'], cd['weight'], cd['skin_color'], cd['hair_color'], cd['profession'], cd['hobbies'], cd['favorite_colors'])
			send_mail(asunto, content, cd['email'], ['elizabeth@elizabetholive.us'])
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
	testimonials = Testimonial.objects.all().order_by('-modify_on')[:2]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'gallery': gallery, 'llamados': llamados}
	return render_to_response('homepage/services.html', ctx, context_instance=RequestContext(request))


def gallery(request):
	success = False
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s Email: %s Phone: %s' % (cd['name'], cd['email'], cd['phone'])
			content = u'Name: %s \nEmail: %s \nPhone: %s \nGender: %s \nHeight: %s \nWeight: %s \nSkin Color: %s \nHair Color: %s \nProfession: %s \nHobbies: %s \nFavorite Colors: %s' % (
				cd['name'], cd['email'], cd['phone'], cd['gender'], cd['height'], cd['weight'], cd['skin_color'], cd['hair_color'], cd['profession'], cd['hobbies'], cd['favorite_colors'])
			send_mail(asunto, content, cd['email'], ['elizabeth@elizabetholive.us'])
	else:
		form = contactForm()
	gallery = GalleryBig.objects.all()[:12]
	entradas = Entry.objects.order_by('-creation_date')
	entradas = entradas[:4]
	testimonials = Testimonial.objects.all()[:3]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials, 'entradas': entradas, 'gallery': gallery}
	return render_to_response('homepage/gallery.html', ctx, context_instance=RequestContext(request))


def contact(request):
	success = False
	if request.method == 'POST':
		form = realcontactForm(request.POST)
		if form.is_valid():
			success = True
			cd = form.cleaned_data
			asunto = u'Por: %s Email: %s Phone: %s' % (cd['name'], cd['email'], cd['phone'])
			content = u'Name: %s \nEmail: %s \nPhone: %s \nGender: %s \nHeight: %s \nWeight: %s \nSkin Color: %s \nHair Color: %s \nProfession: %s \nHobbies: %s \nFavorite Colors: %s \nMessage: %s' % (
				cd['name'], cd['email'], cd['phone'], cd['gender'], cd['height'], cd['weight'], cd['skin_color'], cd['hair_color'], cd['profession'], cd['hobbies'], cd['favorite_colors'], cd['message'])
			send_mail(asunto, content, cd['email'], ['elizabeth@elizabetholive.us'])
	else:
		form = realcontactForm()
	testimonials = Testimonial.objects.all()[:4]
	ctx = {'form': form, 'success': success, 'testimonials': testimonials}
	return render_to_response('homepage/contact.html', ctx, context_instance=RequestContext(request))
