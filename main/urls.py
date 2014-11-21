from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'reminds.views.home', name='home'),
                       url(r'^account/', include('account.urls')),
                       url(r'^account/', include(admin.site.urls)),
                       )
