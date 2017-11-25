"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article import views as art_views  # new
from pic import views as pic_views  # new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', art_views.index,name='home'),  # new
    url(r'^art$', art_views.home, name='home'),  # new
    url(r'^pic$', pic_views.home, name='home'),  # new
    # r'^add/$'是网址显示的名称
    # name的的值是执行函数名
    url(r'^add/$', art_views.add, name='add'),  # 注意修改了这一行
    url(r'^add/(\d+)/(\d+)/$', art_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', art_views.add2, name='add2'),  #使用正则匹配
]
