from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from Home.models import *

# from API.views.user import *
from .view.user import *


def index(request): 
	return HttpResponse("Hey there, This is <b>API</b>  ( from API App ) !!!");  

# def index(request):  
#           pass 


def user(request):
	pass

def signup(request):
	pass

def login(request):
	pass

def logout(request):
	pass















