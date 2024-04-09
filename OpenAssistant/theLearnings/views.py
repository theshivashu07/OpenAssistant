from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import * 
from Home.models import * 

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase 

from _dummydatabase.youtube import YoutubeRUN 
from _dummydatabase.aadhyatm import AadhyatmRUN 


import theLearnings.functions.builder as builder






@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        # print(request.session.get('User',None))
        # for keys,values in request.session.items():
                # print(f"{keys} : {values}")
                
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        return render(request,"theLearnings/Client/learnings-testing.html",ReturningData); 

def learnings_from_(request,skillsof_=None,skills_=None): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        return render(request,"theLearnings/Client/learnings-testing.html",ReturningData); 


		# path('options/<str:skillof>/',views.options,name='options'), 
		# path('<str:skillof>/<str:skill>/',views.skills,name='skills'), 


def options( request,skillof ):
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        return render(request,"theLearnings/Client/skills.html",ReturningData); 



def skills( request,skillof,skill ):
        pass
















