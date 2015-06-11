#!/usr/local/bin/python
# -*- encoding: utf-8 -*-
from django import forms


class HoneypotWidget(forms.TextInput):
	is_hidden = True

	def __init__(self, attrs=None, html_comment=False, *args, **kwargs):
		self.html_comment = html_comment
		super(HoneypotWidget, self).__init__(attrs, *args, **kwargs)
		#if not self.attrs.has_key('class'):
		if not 'class' in self.attrs:
			self.attrs['style'] = 'display:none'

	def render(self, *args, **kwargs):
		value = super(HoneypotWidget, self).render(*args, **kwargs)
		if self.html_comment:
			value = '<!-- %s -->' % value
		return value


class contactForm(forms.Form):
	GENDERS = (('Male', 'male'), ('Female', 'female'),)
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
	phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}))
	email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'nick@email.com'}))
	gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDERS, required=True)
	height = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your height'}))
	weight = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your weight'}))
	skin_color = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Color of your skin'}))
	hair_color = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Color of your hair'}))
	profession = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'What do you do for living?'}))
	hobbies = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'What do you like to do?'}))
	favorite_colors = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Write down all your favorite colors'}))
	website = forms.CharField(widget=HoneypotWidget, required=False)

	def clean_asunto(self):
		cd = self.cleaned_data
		asunto = cd.get('asunto')
		if len(asunto) < 3:
			raise forms.ValidationError("It must be larger than 2 letters.")
		return asunto

	def clean_texto(self):
		cd = self.cleaned_data
		texto = cd.get('texto')
		if len(texto) < 4:
			raise forms.ValidationError("*")
		return texto
