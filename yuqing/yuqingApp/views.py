#encoding:utf-8
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from .forms import AddForm
from yuqingApp.models import User
from django.template.context import RequestContext
import json
# Create your views here.

def index(request):
	return render(request,'home.html')

def create(request):
	if request.method == 'POST':
		user = User.objects.get_or_create(username=request.POST['username'],password=request.POST['password'])
		request.session['user_name'] = request.POST['username']
	return redirect('/welcome/')

def login_session(request):
	form = AddForm(request.POST)
	if form.is_valid():
		if User.objects.filter(username=form.cleaned_data['username']).exists():
			user = User.objects.get(username=form.cleaned_data['username'])
			if user.password == form.cleaned_data['password']:
				request.session['user_name'] = user.username
				return redirect('/welcome/')
			else:
				return render_to_response('index.html',RequestContext(request,{'password_is_wrong':True}))
		else:
			return render_to_response('index.html',RequestContext(request,{'username_is_wrong':True}))

def logout(request):
	try:
		del request.session['user_name']
	except KeyError:
		pass
	return redirect('/')

def welcome(request):
	return render(request,'welcome.html')

def search(request):
	data = [
			{ 
				'time':request.POST.getlist('time'),
				'meiti':request.POST.getlist('meiti'),
				'guanjianci':request.POST['guanjianci'],
				'paichuguanjianci':request.POST['paichuguanjianci'] 
			}
		]
	return HttpResponse(data)