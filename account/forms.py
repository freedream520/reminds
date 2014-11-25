#-*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label=u'用户名', min_length=3, max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm',
                                                             'required': True}))
    email = forms.EmailField(label=u'联系邮箱',
                             widget=forms.TextInput(attrs={'placeholder': '填写真实邮箱用于重置密码',
                                                           'class': 'form-control input-sm',
                                                           'required': True}))
    password = forms.CharField(label=u'密码', min_length=6, max_length=16,
                               widget=forms.PasswordInput(attrs={'class': 'form-control input-sm',
                                                                 'required': True}))
    password_ = forms.CharField(label=u'确认密码', min_length=6, max_length=16,
                                widget=forms.PasswordInput(attrs={'class': 'form-control input-sm',
                                                                  'required': True}))

    def clean_password(self):
        '''
            验证密码长度
        '''
        pwd = self.cleaned_data.get('password')
        if not 6 <= len(pwd) <= 16:
            raise forms.ValidationError(u'密码长度应为6-16个字符！')
        return pwd

    def clean_password_(self):
        '''
            验证密码是否相同
        '''
        pwd = self.cleaned_data.get('password_')
        if pwd != self.cleaned_data.get('password'):
            raise forms.ValidationError(u'密码不一致！')
        return pwd

    def clean_username(self):
        '''
            验证用户名是否已被注册
        '''
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'该用户名已被注册！')


class ResetPasswordForm(forms.Form):

    """
        忘记密码，重置密码表单
    """
    password = forms.CharField(label=u'新的密码', widget=forms.PasswordInput(), max_length=16, min_length=6, required=True)
    password_ = forms.CharField(label=u'确认密码', widget=forms.PasswordInput(), max_length=16, required=True, min_length=6)

    def clean_password(self):
        '''
            验证密码1长度
        '''
        p1 = self.cleaned_data.get('password')
        if not 6 <= len(p1) <= 16:
            raise forms.ValidationError(u'密码长度应为6-16个字符！')
        return p1

    def clean_password_(self):
        '''
            验证密码2是否等于密码1
        '''
        p2 = self.cleaned_data.get('password_')
        if self.cleaned_data.get('password') != p2:
            raise forms.ValidationError(u'密码不一致！')
        return p2


class ForgetPasswordForm(forms.Form):

    """
        忘记密码，注册信息表单
    """
    username = forms.CharField(label=u'用户名', min_length=3, max_length=20, required=True)
    email = forms.EmailField(label=u'注册邮箱', required=True)

    def clean_username(self):
        '''
            验证用户名是否存在
        '''
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            return username
        except User.DoesNotExist:
            raise forms.ValidationError(u'团队名称不存在！')
