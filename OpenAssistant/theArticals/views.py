from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from Home.models import *

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase

# from _dummydatabase.youtube import YoutubeRUN
# from _dummydatabase.aadhyatm import AadhyatmRUN
# from _dummydatabase.problems import ProblemsRUN
from _dummydatabase.articals import ArticalsRUN

from theArticals.functions import get as function_get




@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        # return render(request,"thearticals/client/articals.html",ReturningData); 
        return render(request,"thearticals/client/articals-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/")
def articals_from_(request,from_):         
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        # return render(request,"thearticals/client/articals.html",ReturningData); 
        return render(request,"thearticals/client/articals-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/")
def open(request,slug):
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticals(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        # return render(request,"thearticals/client/articals.html",ReturningData); 
        return render(request,"thearticals/client/articals-open.html",ReturningData); 

# @LoginRequired(login_url="/security/login/")
def write(request,id=None):
        ReturningData = dict()
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        if id:
                return render(request,"thearticals/client/articals-write.html",ReturningData); 
        return render(request,"thearticals/client/articals-write-base.html",ReturningData); 







