from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return HttpResponse('Home page')
    return render(request, './index.html', context={'title': 'Django example', 'name': 'Weihao'})

# 文件路径得弄对,并且写相对路径
# request是请求对象
