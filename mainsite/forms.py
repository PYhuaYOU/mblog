#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from mainsite import models

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=10)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

class ContactForm(forms.Form):
    CITY = [
        ['SH', 'Shanghai'],
        ['GZ', 'Guangzhou'],
        ['NJ', 'Nanjing'],
        ['WH', 'Wuhan'],
        ['NA', 'others']
    ]

    user_name = forms.CharField(label='你的姓名',max_length=50,initial='李大仁')
    user_city = forms.ChoiceField(label='居住城市',choices=CITY)
    user_school = forms.BooleanField(label='是否在学',required=False)
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='你的意见',widget=forms.Textarea)

from captcha.fields import CaptchaField
class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Post
        fields = ['title', 'slug', 'body']

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['title'].label = '标题'
        self.fields['body'].label ='文章'
        self.fields['captcha'].label='确定你不是机器人'