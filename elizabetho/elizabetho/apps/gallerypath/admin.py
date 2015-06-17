from django.contrib import admin
from .models import Gallery, Image


class ImageInline(admin.TabularInline):
	model = Image


class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title', 'path', 'creado_en', 'modificado_en',)
	list_display_links = ('title',)
	list_filter = ('creado_en', 'modificado_en',)
	search_fields = ['titulo', 'path']
	inlines = [
		ImageInline,
	]


class ImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'gallery', 'url_to', 'alt', 'creado_en', 'modificado_en',)
	list_display_links = ('title',)
	list_filter = ('tipo', 'creado_en', 'modificado_en', 'url_to')
	search_fields = ['titulo', 'url_to', 'alt']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image)
