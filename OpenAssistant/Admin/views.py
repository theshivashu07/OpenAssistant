
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from Client.models import *
from Home.models import *

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase

from Client._dummydatabase.youtube import YoutubeRUN
from Client._dummydatabase.articals import ArticalsRUN
from Client._dummydatabase.problems import ProblemsRUN
from Client._dummydatabase.aadhyatm import AadhyatmRUN


# def index(request):
# 	return HttpResponse("Hey there, This is <b>Developer</b>  ( from Admin App ) !!!");




@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"developer/index.html",ReturningData); 

# def index(request): 
# 	if not request.user.is_authenticated:
# 		return redirect("security/") 
# 	return render(request,"developer/index.html"); 



@LoginRequired(login_url="/security/login/")
def articals(request): 
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"developer/articals.html",ReturningData); 
        return render(request,"developer/articals-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/")
def articals_from_(request,from_):         
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"developer/articals.html",ReturningData); 
        return render(request,"developer/articals-testing.html",ReturningData); 




@LoginRequired(login_url="/security/login/")
def problems(request): 
        ReturningData = dict()
        ProblemsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"developer/problems.html",ReturningData); 
        return render(request,"developer/problems-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/") 
def problems_from_(request,from_): 
        ReturningData = dict()
        ProblemsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        # return render(request,"developer/problems.html",ReturningData); 
        return render(request,"developer/problems-testing.html",ReturningData); 






@LoginRequired(login_url="/security/login/")
def youtube(request): 
        ReturningData = dict()
        YoutubeRUN( limit=4, dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        return render(request,"developer/youtube.html",ReturningData); 
        # return render(request,"developer/youtube-testing.html",ReturningData); 

def youtube_from_(request,from_): 
        ReturningData = dict()
        YoutubeRUN( limit=4, dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        return render(request,"developer/youtube.html",ReturningData); 
        # return render(request,"developer/youtube-testing.html",ReturningData); 






@LoginRequired(login_url="/security/login/")
def aadhyatm(request): 
        ReturningData = dict()
        AadhyatmRUN( dictionary=ReturningData )
        ReturningDatabase( request,ReturningData )
        # return render(request,"developer/aadhyatm.html",ReturningData); 
        return render(request,"developer/aadhyatm-testing.html",ReturningData); 

def aadhyatm_from_(request,from_): 
        ReturningData = dict()
        AadhyatmRUN( dictionary=ReturningData )
        ReturningDatabase( request,ReturningData )
        # return render(request,"developer/aadhyatm.html",ReturningData); 
        return render(request,"developer/aadhyatm-testing.html",ReturningData); 





@LoginRequired(login_url="/security/login/")
def hireus(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        print(request.session.get('User',None))
        for keys,values in request.session.items():
                print(f"{keys} : {values}")
        return render(request,"developer/hireus.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def notifications(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"developer/notifications.html",ReturningData); 






@LoginRequired(login_url="/security/login/")
def profile(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"developer/profile.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def profile_edit(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"developer/profile_edit.html",ReturningData); 













