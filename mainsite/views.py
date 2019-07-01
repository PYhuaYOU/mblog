from django.shortcuts import render,redirect
from mainsite import models
# Create your views here.
from .models import Post
from django.http import HttpResponse
from datetime import datetime
from django.contrib.sessions.models import Session

def deleshu(request,slug):
    # form = forms.PostForm()
    # ret = form.cleaned_data['slug']
    post = Post.objects.filter(slug=slug).first()
    print('ok')
    if post:
        post.delete()
        # post.save()
        message='数据删除成功'
    return render(request,'index.html',locals())

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request,'index.html',locals())#locals()把当前所有局部变量打包成字典类型

    # post_list = list()
    # for count, post in enumerate(posts):
    #     post_list.append("NO.%s"%count + str(post)+ "<br>")
    #     post_list.append("<h3>" +str(post.body) +"</h3><br>")
    # return HttpResponse(post_list)

def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        if post:
            return render(request,'post.html',locals())
    except:
        redirect("index/")

def Login(request):
    # user = request.GET.get('user_id', None)
    # # user = request.GET['user_id']
    # password = request.GET.get('user_pass', None)
    # print(user, password)
    # if user=='you' and password=='123':
    #     print('OK')
    # #
    #     return redirect("/contact/")
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = models.User.objects.get(name=login_name)
                if user.password == login_password:
                    request.session['username']=user.name
                    print(request.session['username'])
                    return redirect('/post2db/')
                else:
                    message = '密码错误'
            except:
                message='找不到用户'
        else:
            message='检查'
    else:
        login_form = forms.LoginForm()

    return render(request,'login.html', locals())

from mainsite import forms

def contact(request):
    if 'username' in request.session.keys():
        username = request.session['username']
        if request.method == 'POST':

            form=forms.ContactForm(request.POST)
            if form.is_valid():
                message = "感谢"
                user_name = form.cleaned_data['user_name']
                # return redirect("/index/")
            else:
                message = '检查'
        else:
            form = forms.ContactForm()
        return render(request, 'contact.html', locals())
    else:
        return redirect('/login/')

def post2db(request):
    if 'username' in request.session.keys():
        username = request.session['username']
        print(username)
        if request.method =='POST':
            form = forms.PostForm(request.POST)
            if form.is_valid():
                form.save()
                message = '保存'
                return redirect('/index/')
            else:

                message = '填写信息'
        else:
            message = '填写信息'
            form = forms.PostForm()
        return render(request,'post2db.html',locals())
    else:
        return redirect('/login/')

def logout(request):
    if 'username' in request.session.keys():
        Session.objects.all().delete()
        return redirect('/login/')



