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

from API.Code.Management.Sessions import *


@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 
        # return render(request,"thearticals/client/articals.html",ReturningData); 
        return render(request,"thearticals/client/articals-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/")
def articals_from_(request,from_):         
        ReturningData = dict() 
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 
        # return render(request,"thearticals/client/articals.html",ReturningData); 
        return render(request,"thearticals/client/articals-testing.html",ReturningData); 

# @LoginRequired(login_url="/security/login/")
def open(request,slug):
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 
        # return render(request,"thearticals/client/articals.html",ReturningData); 
        return render(request,"thearticals/client/articals-open.html",ReturningData); 



# @LoginRequired(login_url="/security/login/")
def write(request):
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 



        # there is we check if we are have ".../write/tag=h1/
        datasets = checkWritingWith(request)
        if datasets:
                

                
                return render(request,"thearticals/client/articals-write.html",ReturningData); 

        ReturningData['skills'] = function_get.getSkillsets(request) 
        return render(request,"thearticals/client/articals-write.html",ReturningData); 



def writesetup(request):
        
        ReturningData = dict()
        
        if request.method == "POST":
                
                user = UserExists(request)
                # get all fields values to a variables
                title = request.POST.get( 'title',None )
                skill = request.POST.get( 'skill',None )
                discription = request.POST.get( 'discription',None ) 
                # filter id's skills data from database
                skill = SkillSetsBuild.objects.get( pk=skill )

                # we make new Artical's object 
                ArticalsObject = Articals() 
                ArticalsObject.USER = user 
                ArticalsObject.SkillSetsBuild = skill 
                ArticalsObject.title = title 
                ArticalsObject.discription = discription 
                ArticalsObject.save() 


                # we get back user's single available object, and if not available make immidiate 
                RunningNewArticalsObject = RunningNewArticals.objects.filter( USER=user )
                if not RunningNewArticalsObject:
                        RunningNewArticalsObject = RunningNewArticals()
                        RunningNewArticalsObject.USER = user
                        RunningNewArticalsObject.save()
                else:
                        RunningNewArticalsObject = RunningNewArticalsObject[0]
                # now we setup new artical's original data to a Articals 
                RunningNewArticalsObject.artical = ArticalsObject
                RunningNewArticalsObject.content = dict
                RunningNewArticalsObject.save()

                # dummy data, try to think write that..... #testingphase 
                RunningNewArticalsObject.content = {
                        1 : {
                                'contentfrom' : 'tag',
                                'contentof' : 'h1',
                                'content' : {
                                        'title' : None
                                },
                        },
                        2 : {
                                'contentfrom' : 'tag',
                                'contentof' : 'span',
                                'content' : {
                                        'title' : None
                                },
                        },
                        3 : {
                                'contentfrom' : None,
                                'contentof' : None,
                                'content' : {
                                },
                        },
                }
                RunningNewArticalsObject.save()

                return redirect("/articals/write/")


        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 

        ReturningData['skills'] = function_get.getSkillsets(request) 
        return render(request,"thearticals/client/articals-write-base.html",ReturningData); 







# @LoginRequired(login_url="/security/login/")
def writerunning(request):
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)

        HeaderDatabase(request,ReturningData)

        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 


def HeaderDatabase(request,database):
        data = {
                'bgcolor' : "rebeccapurple",
                'path' : '/articals/',
                'active-app' : 'articals',
                'user' : {
                        'name' : "SHivam SHukla",
                        'username' : "theshivashu", 
                        'profile' : "/_uploads/_user/_profiles/default.jpeg", 
                        'path' : "/profile/"
                }
        }
        return data


















####################################################################
# NextLevelFunctions


def checkWritingWith(request):  
        '''this is the function who help us to know coming write url have tags or features t implement or not '''  

        tag = request.GET.get('tag',None) 
        feature = request.GET.get('feature',None)  

        data = None
        if tag: 
                data = { 
                        'contentfrom' : 'tag', 
                        'contentof' : tag, 
                } 
        elif feature: 
                data = { 
                        'contentfrom' : 'feature', 
                        'contentof' : feature, 
                } 

        return data 


content = {
        '1' : {
                'contentfrom' : "",
                'contentof' : "h1",
                'data' : {
                        'title' : None, 
                },
        },
}




