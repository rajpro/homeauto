from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requet):
	return HttpResponse("<h1>Hello Veronica</h1>")

def working(requet):
	return HttpResponse("<h1>Working Veronica</h1>")