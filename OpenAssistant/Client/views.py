from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *



def index(request):
	return HttpResponse("Hey there, This is <b>User</b>  ( from Client App ) !!!");

# def index(request): 
#           pass




