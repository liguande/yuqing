#encoding:utf-8
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from .forms import AddForm
from yuqingApp.models import User
from django.template.context import RequestContext
# Create your views here.

def index(request):
	form = AddForm()
	return render(request,'home.html',{'form':form})

def create(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			info = form.cleaned_data
			user = User.objects.get_or_create(username=info['username'],password=info['password'])
	alluser = User.objects.all()
	return render(request,'welcome.html',{ 'alluser':alluser })

def login_session(request):
	form = AddForm(request.POST)
	if form.is_valid():
		if User.objects.filter(username=form.cleaned_data['username']).exists():
			user = User.objects.get(username=form.cleaned_data['username'])
			if user.password == form.cleaned_data['password']:
				request.session['user_name'] = user.username
				return redirect('/welcome/')
			else:
				return render_to_response('index.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
		else:
			return render_to_response('index.html',RequestContext(request,{'form':form,'username_is_wrong':True}))

def logout(request):
	try:
		del request.session['user_name']
	except KeyError:
		pass
	return redirect('/')
def welcome(request):
	return render(request,'welcome.html')

