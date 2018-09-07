from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib import messages
from .forms import RoomForm
from .models import Room

# Create your views here.

def room_index(request):

	# Check for authentication
	if not request.user.is_authenticated:
		return redirect('/')

	# Sending Data from view.py to all Templates
	cd = {}
	cd['page_title'] = "Room"
	cd['menu_active'] = ""
	cd['box_title'] = "List all Rooms"
	cd['models'] = Room.objects.all() # Fetch All data from Tabel "room_room"
	# Parse Template
	cd['dash_index'] = get_template('room/room_index.html').render(cd)
	return render(request,'common/index.html',{'data':cd})

def room_add(request):

	# Check for authentication
	if not request.user.is_authenticated:
		return redirect('/')

	# Sending Data from view.py to all Templates
	cd = {}
	cd['page_title'] = "Room"
	cd['menu_active'] = ""
	cd['box_title'] = "Add Rooms"

	# Check whether we get post data or not
	# and then save it.
	if request.method == "POST":
		form = RoomForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				messages.add_message(request, messages.SUCCESS, 'A New Room Added Successfully.')
				return redirect('/room/room_add')
			except:
				pass
	# Parse Template
	cd['forms'] = RoomForm()
	cd['dash_index'] = get_template('room/room_add.html').template.render(RequestContext(request, cd))
	return render(request,'common/index.html',{'data':cd})

def room_update(request,id):

	# Check for authentication
	if not request.user.is_authenticated:
		return redirect('/')

	# Sending Data from view.py to all Templates
	cd = {}
	cd['page_title'] = "Room"
	cd['menu_active'] = ""
	cd['box_title'] = "Update Rooms"
	# Get All data of a perticula ID
	cd['models'] = Room.objects.get(id=id)

	# Check whether we get post data or not
	# and then Update it.
	if request.method == "POST":
		form = RoomForm(request.POST,instance=cd['models'])
		if form.is_valid():
			try:
				form.save()
				messages.add_message(request, messages.SUCCESS, 'A New Room Updated Successfully.')
				return redirect('/room/')
			except:
				pass

	# Parse Template
	cd['dash_index'] = get_template('room/room_update.html').template.render(RequestContext(request, cd))
	return render(request,'common/index.html',{'data':cd})

def room_delete(request):
	if not request.user.is_authenticated:
		return redirect('/')
	cd = {}
	cd['dash_index'] = get_template('room/room_index.html').render()
	return render(request,'common/index.html',{'data':cd})