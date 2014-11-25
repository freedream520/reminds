#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from forms import *
from django.template import RequestContext

def register(request):
    '''
        用户注册视图
    '''
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            #user.is_active = False
            user.save()

            messages.add_message(request, messages.INFO, u'注册成功！')
            return HttpResponseRedirect('/account/')

    return render_to_response('account/register.html', {'form':form, }, context_instance=RequestContext(request))
