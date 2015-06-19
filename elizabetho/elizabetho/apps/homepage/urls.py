from django.conf.urls import patterns, url

urlpatterns = patterns(
	'elizabetho.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^about/$', 'about', name="homepageabout"),
	url(r'^services/$', 'services', name="homepageservices"),
	url(r'^gallery/$', 'gallery', name="homepagegallery"),
	url(r'^contact/$', 'contact', name="homepagecontact"),
)
