#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import Permission
from django.contrib.auth import logout
from django.contrib.auth.models import User
from account import forms as account_forms
from account.models import ResetPasswordCode
import tools
from django.utils import timezone
from mailer import send_email
from main.settings import DOMAIN


def register(request):
    form = account_forms.RegisterForm()
    if request.method == 'POST':
        form = account_forms.RegisterForm(request.POST)
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


def forgotpassword(request):
    form = account_forms.ForgetPasswordForm()
    if request.method == 'POST':
        form = account_forms.ForgetPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = get_object_or_404(User, username=cd['username'])
            if user.email == cd['email']:
                reset_password_code = tools.get_reset_password_code(user)
                reset_expires = timezone.localtime(timezone.now()) + timezone.timedelta(1)
                code, _ = ResetPasswordCode.objects.get_or_create(user=user)
                code.reset_password_code = reset_password_code
                code.reset_expires = reset_expires
                code.save()
                info = u'点击链接 %s/account/resetpassword/%s 重置您的密码。【Reminds】' % (DOMAIN, reset_password_code)
                send_email(user.email, u'Reminds重置密码', info)
                email_url = tools.get_email_url(user.email)
                messages.add_message(
                    request,
                    messages.INFO,
                    u'重置密码链接已发送至你的<a href="http://%s" target="_blank">邮箱</a>，\
                    请注意查收！' % email_url)
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    u'邮箱错误！')

    return render_to_response(
        'account/forgotpassword.html',
        {'form': form, },
        context_instance=RequestContext(request))


def resetpassword(request, reset_password_code):
    code = get_object_or_404(ResetPasswordCode, reset_password_code=reset_password_code)
    if code.reset_expires < timezone.localtime(timezone.now()):
        messages.add_message(request, messages.INFO, u'重置密码有效期限已过！')
        return HttpResponseRedirect('/account/')

    form = account_forms.ResetPasswordForm()
    if request.method == "POST":
        form = account_forms.ResetPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = code.user
            user.set_password(cd['password'])
            user.save()
            messages.add_message(request, messages.INFO, u'密码重置成功，请重新登录！')
            return HttpResponseRedirect('/account/')

    return render_to_response(
        'account/resetpassword.html',
        {'form': form, },
        context_instance=RequestContext(request))
