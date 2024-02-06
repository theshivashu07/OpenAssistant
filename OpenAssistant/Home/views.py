import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth import authenticate as Authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required as LoginRequired

from django.contrib import messages
from .models import *






def index(request):
	return HttpResponse("Hey there, This is <b>Client</b>  ( from Home App ) !!!");




import API.Views.User.SignUp as dbSignUp
def signup(request): 
	dbSignUp.SignUp(
		
	)





