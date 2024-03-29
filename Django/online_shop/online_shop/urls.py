"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) # 引入应用的子路由
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from stu import views  # 需要使用.来表示模块在当前目录

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.login_view, name='login_view'),
]
