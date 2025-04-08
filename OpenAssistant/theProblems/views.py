from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from Home.models import *

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase

# from _dummydatabase.youtube import YoutubeRUN
# from _dummydatabase.articals import ArticalsRUN
# from _dummydatabase.aadhyatm import AadhyatmRUN
from _dummydatabase.problems import ProblemsRUN






@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        ProblemsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"theproblems/client/problems.html",ReturningData); 
        return render(request,"theproblems/client/problems-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/") 
def problems_from_(request,from_): 
        ReturningData = dict()
        ProblemsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"theproblems/client/problems.html",ReturningData); 
        return render(request,"theproblems/client/problems-testing.html",ReturningData); 


# @LoginRequired(login_url="/security/login/") 
def openproblem(request): 
        ReturningData = dict()
        ProblemsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"theproblems/client/problems.html",ReturningData); 
        # return render(request,"theproblems/client/problems-open.html",ReturningData); 
        return render(request,"theproblems/client/problems-open-new.html",ReturningData); 
        # return render(request,"theproblems/client/problems-solution-only.html",ReturningData); 







