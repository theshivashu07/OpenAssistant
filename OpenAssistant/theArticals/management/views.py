from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from theArticals.models import *
from Home.models import *

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase

# from _dummydatabase.youtube import YoutubeRUN
# from _dummydatabase.aadhyatm import AadhyatmRUN
# from _dummydatabase.problems import ProblemsRUN
from _dummydatabase.articals import ArticalsRUN

from theArticals.functions import get as function_get

from API.Code.Management.Sessions import *

from API.models import Skills,SkillsOf, SkillsGroup, SkillSetsBuild




def CollectingData(*args,**kwargs):
        pass


@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        CollectingData( dictionary=ReturningData )
        
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['DefaultArticalsList'] = function_get.getDefaultArticalsList(request)
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = function_get.getSidebarLeftDetails(request) 
        return render(request,"thearticals/client/articals-testing.html",ReturningData); 

