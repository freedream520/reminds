from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'reminds.views.home', name='home'),
                       url(r'^account/', include('account.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
