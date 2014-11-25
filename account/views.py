#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import Permission
from django.contrib.auth import logout


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password'])
            user.is_staff = True
            can_add = Permission.objects.get(name='Can add remind')
            can_change = Permission.objects.get(name='Can change remind')
            can_delete = Permission.objects.get(name='Can delete remind')
            user.user_permissions = [can_add, can_change, can_delete]
            user.save()
            logout(request)
            messages.add_message(
                request,
                messages.INFO,
                u'注册成功，请登录！')
            return HttpResponseRedirect('/account/')

    return render_to_response(
        'account/register.html',
        {'form': form, },
        context_instance=RequestContext(request))
