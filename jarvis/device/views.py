from django.shortcuts import render, redirect
from django.template.loader import get_template

# Create your views here.

def device_index(request):
	if not request.user.is_authenticated:
		return redirect('/')
	cd = {}
	cd['dash_index'] = get_template('rooms/rooms_index.html').render()
	return render(request,'common/index.html',{'data':cd})

def device_add(request):
	if not request.user.is_authenticated:
		return redirect('/')
	cd = {}
	cd['dash_index'] = get_template('rooms/rooms_index.html').render()
	return render(request,'common/index.html',{'data':cd})

def device_update(request):
	if not request.user.is_authenticated:
		return redirect('/')
	cd = {}
	cd['dash_index'] = get_template('rooms/rooms_index.html').render()
	return render(request,'common/index.html',{'data':cd})

def device_delete(request):
	if not request.user.is_authenticated:
		return redirect('/')
	cd = {}
	cd['dash_index'] = get_template('rooms/rooms_index.html').render()
	return render(request,'common/index.html',{'data':cd})