from django.shortcuts import render

from django.http import HttpResponse

from django.urls import reverse

from django.http import HttpResponseRedirect
# Create your views here.

# 添加模板文件
def home(request):
    return render(request, 'index.html')