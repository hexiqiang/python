# 引入模板模块
from django.shortcuts import render

from django.http import HttpResponse

from django.urls import reverse

from django.http import HttpResponseRedirect
# Create your views here.

# 添加模板文件
def home(request):
    return render(request, 'home.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = a + b
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )