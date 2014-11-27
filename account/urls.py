from django.conf.urls import *

urlpatterns = patterns(
    '',
    url(r'^register/$', 'account.views.register', name='register'),
    url(r'^forgotpassword/$', 'account.views.forgotpassword', name='forgotpassword'),
    url(r'^resetpassword/(?P<reset_password_code>\w{40})/$', 'account.views.resetpassword', name='resetpassword'),
)
