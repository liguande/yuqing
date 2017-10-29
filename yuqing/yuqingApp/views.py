#encoding:utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AddForm
from yuqingApp.models import User
# Create your views here.

def index(request):
	return render(request,'home.html')

def new(request):
	form = AddForm()
	return render(request,'new_user.html',{'form':form})

def create(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			info = form.cleaned_data
			user = User.objects.get_or_create(username=info['username'],password=info['password'])
	alluser = User.objects.all()
	return render(request,'welcome.html',{ 'alluser':alluser })

def login(request):
	form = AddForm()
	return render(request,'login.html',{'form':form})

def login_session(request):
	form = AddForm(request.POST)
	if form.is_valid():
		if User.objects.filter(username=form.cleaned_data['username']).exists():
			user = User.objects.get(username=form.cleaned_data['username'])
			if user.password == form.cleaned_data['password']:
				request.session['user_name'] = user.username
				return redirect('/welcome/')
			else:
				return render(request,'login.html',{'form':form})
		else:
			return render(request,'login.html',{'form':form})

def welcome(request):
	return render(request,'welcome.html')