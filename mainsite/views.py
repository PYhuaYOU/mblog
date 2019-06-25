from django.shortcuts import render,redirect

# Create your views here.
from .models import Post
from django.http import HttpResponse
from datetime import datetime

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