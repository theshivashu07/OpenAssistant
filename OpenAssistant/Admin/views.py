from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *



def index(request):
	return HttpResponse("Hey there, This is <b>Developer</b>  ( from Admin App ) !!!");

# def index(request): 
#           pass




