from django.conf.urls import *

urlpatterns = patterns('',
                       url(r'^register/$', 'account.views.register', name='register'),
                       )
