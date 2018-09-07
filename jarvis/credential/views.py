
# imports
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def cred_index(request):
	if request.user.is_authenticated:
		return redirect('/dashboard/')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/dashboard/')
		else:
			messages.add_message(request, messages.WARNING, 'Your Username or Password is wrong.')
			return redirect('/')
	return render(request,'login.html')

def cred_logout(request):
	logout(request)
	return redirect('/')

def cred_profile(request):
	logout(request)
	return redirect('/')

def cred_change_password(request):
	logout(request)
	return redirect('/')