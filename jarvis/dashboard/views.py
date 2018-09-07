from django.shortcuts import render, redirect
from django.template.loader import get_template

# Create your views here.

def dash_index(request):
	if not request.user.is_authenticated:
		return redirect('/')
	cd = {}
	cd['page_title'] = "Dashboard"
	cd['dash_index'] = get_template('dashboard/dash_index.html').render()
	return render(request,'common/index.html',{'data':cd})