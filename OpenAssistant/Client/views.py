from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from Home.models import *


# def index(request):
# 	return HttpResponse("Hey there, This is <b>User</b>  ( from Client App ) !!!");

def getpaths(request): 
          from django.core.management.commands.runserver import Command as runserver  
          base_path = f"{runserver.default_addr}:{runserver.default_port}"
def index(request): 
          # getpaths(request)
          return redirect("security/") 
          if not request.session.get('user',None): 
                  return redirect("security/") 
          return render(request,"client/index.html"); 

# def index(request): 
# 	if not request.user.is_authenticated:
# 		return redirect("security/") 
# 	return render(request,"client/index.html"); 






