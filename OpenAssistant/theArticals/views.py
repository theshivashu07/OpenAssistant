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

from API.models import Skills,SkillsOf, SkillsGroup, SkillSetsBuild





@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        # ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['DefaultArticalsList'] = function_get.getDefaultArticalsList(request)
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = function_get.getSidebarLeftDetails(request) 
        return render(request,"thearticals/client/articals-testing.html",ReturningData); 


def adda(request,*args,**kwargs):
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['DefaultArticalsList'] = function_get.getDefaultArticalsList(request)
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request)
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = function_get.getSidebarLeftDetails(request) 
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
def open(request,*args,**kwargs):
        skill = kwargs.get( 'skill', request.GET.get( 'skill',None ) )
        artical = kwargs.get( 'artical', request.GET.get( 'artical',None ) )
        
        ReturningData = dict()
        ReturningDatabase(request,ReturningData) # USER Header

        ReturningData['Articals'] = dict() 
        
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 

        # Actually SkillSetsBuild's slug is exect same as Skills slug !!! 
        skillsetsbuild = SkillSetsBuild.objects.filter( slug=skill )[0]
        # we get all related SkillsPointers's and then check their related slug !!!
        skillspointers = SkillsPointers.objects.filter( skillsetbuild=skillsetsbuild )
        print(skillspointers)

        for skillspointer in skillspointers: 
                object = Articals.objects.filter( skillspointers=skillspointer,slug=artical ) [0]
                ReturningData['Articals']['Content'] = object 
                break
        
        return render(request,"thearticals/client/articals-show.html",ReturningData);  



# @LoginRequired(login_url="/security/login/")
def write(request):
        ReturningData = dict()
        ArticalsRUN( dictionary=ReturningData)
        ReturningDatabase(request,ReturningData)
        ReturningData['Articals'] = dict() 
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 

        ReturningData['skills'] = function_get.getSkillsets(request) 
        if request.method == "POST":
                return redirect('/articals/show/')
        return render(request,"thearticals/client/articals-write.html",ReturningData); 



def show(request):
        
        ReturningData = dict()
        ReturningDatabase(request,ReturningData) # USER Header
        ReturningData['Articals'] = dict() 
        
        ReturningData['Articals']['OpenedArticals'] = function_get.getOpenedArticalsDetails(request) 
        ReturningData['Articals']['RecentArticalsList'] = function_get.getRecentArticalsList(request) 
        ReturningData['Articals']['Scrollbar'] = function_get.getScrollbarDetails(request) 

        user = UserExists(request)
        artical = Articals.objects.filter( USER=user )[::-1][0]
        ReturningData['Articals']['Content'] = artical
        return render(request,"thearticals/client/ckeditor.html",ReturningData); 
        return render(request,"thearticals/client/articals-show.html",ReturningData); 


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

















def ShowByOption(request,optionname): 
        return redirect('/articals/')  





def ShowRelatedArticals(request,skillsetsbuild):
        user = UserExists(request)
        skillsetsbuild = '-'.join( skillsetsbuild.split('-')[1:] )
        skills = Skills.objects.get( name=skillsetsbuild )
        skillsetsbuild = SkillSetsBuild.objects.get( skills=skills )
        return




def ShowMyArtical(request,skillsetsbuild,skillspointers):
        user = UserExists(request)


        return




























