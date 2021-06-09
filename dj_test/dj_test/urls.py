"""dj_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from upload_app import views

from django.shortcuts import HttpResponse, render

urlpatterns = [
    path('admin/', admin.site.urls),
    path("app01/", include("aoo01.urls", namespace="app01")),
    path("app02/", include("aoo02.urls", namespace="app02")),
    path('upload/', views.Upload.as_view()),
    path('index2/', views.index, name="main"),
    path("index1/", views.index1),
    re_path(r"^go/$", views.go),  # $终止符前结尾 ^起始符以后开始
    re_path(r"^go/2020/$", views.go2),
    path("do/<int:year>/<int:month>", views.go3, name="do_it"),
]
