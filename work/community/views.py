from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from community import models
from django import forms
from django.forms import  Form, fields, widgets
from django.template import RequestContext
# Create your views here.
CHOICE = [1,2,3,4,5]
class UserForm(forms.Form):
    username = forms.CharField(label='名字',max_length=24)
    userpassword = forms.CharField(label='密码',max_length=24)
def index(requset):
    username = requset.COOKIES.get('cookie_username', '')
    return render(requset,'index.html',{'username':username})
def register(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request, 'register.html', {'obj': obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            username = obj.cleaned_data['username']
            password = obj.cleaned_data['userpassword']
            models.user_info.objects.create(user_name=username,user_password=password)
            return render(request, 'register1.html', {'us': username} )

def login(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request,'login.html',{'obj':obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            username = obj.cleaned_data['username']
            password = obj.cleaned_data['userpassword']
            a = models.user_info.objects.filter(user_name__exact=username,user_password__exact=password)
            if a:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('cookie_username', username, 3600)
                return response
            else:
                b = '登陆失败！'
                return render(request,'login.html',{'b':b})
        #return render(request,'login.html',{'obj':obj})
def logout(request):
    response = HttpResponse('logout!!!')
    response.delete_cookie('cookie_username')
    return response
def person(request):
    a = HttpResponse('text')
    username = a.cookies.get('cookie_username', '')
    return a