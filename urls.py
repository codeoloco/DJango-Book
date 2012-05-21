from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from mysite.books import views
from mysite.contacts import views as contact_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^displaymeta/$', display_meta),
    (r'^search/$', views.search),
    (r'^contact/$', contact_views.contact),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
