from django.conf.urls import *

urlpatterns = patterns(
    '',
    url(r'^register/$', 'account.views.register', name='register'),
    url(r'^forgotpassword/$', 'account.views.forgotpassword', name='forgotpassword'),
)
