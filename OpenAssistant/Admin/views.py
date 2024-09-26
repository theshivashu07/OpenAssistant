
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from Client.models import *
from Home.models import *

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase

# from _dummydatabase.articals import ArticalsRUN
# from _dummydatabase.problems import ProblemsRUN
# from _dummydatabase.youtube import YoutubeRUN
# from _dummydatabase.aadhyatm import AadhyatmRUN


def index(request):
	return HttpResponse("Hey there, This is <b>Developer</b>  ( from Admin App ) !!!");















