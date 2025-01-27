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
import theLearnings.functions.ShortTime as ShortTime





@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict() 
        ReturningDatabase(request,ReturningData)
        
        skill = request.GET.get("skill",None)
        if skill:
                skillobj = Skill.objects.filter(name__iexact=skill)
                if skillobj:
                        topics = TopicHeadings.objects.filter( skill=skillobj.first() )
                else:
                        return redirect(request.path)
                ReturningData['topics'] = topics 
                ReturningData['Articals'] = dict()
                ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
                ReturningData['Articals']['skills'] = builder.getSidebarLeftDetails_forApp(request) 
                
                skillObject = Skill.objects.filter(name__iexact=skill)[0]
                print(skillObject)
                ReturningData['skill'] = skillObject 
                ReturningData['topics'] = ShortTime.getTopics(request,skillObject) 

                return render(request,"theLearnings/Client/landing-page-2-skills-list.html",ReturningData); 

        
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        # ReturningData['Articals']['skills'] = builder.getSidebarLeftDetails_forApp(request) 
        
        ReturningData['skills'] = ShortTime.getSkills(request)

        return render(request,"theLearnings/Client/landing-page.html",ReturningData); 
        # return render(request,"theLearnings/Client/learnings-testing.html",ReturningData); 

def learnings_from_(request,skillsof_=None,skills_=None): 
        ReturningData = dict() 
        ReturningDatabase(request,ReturningData) 

        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        return render(request,"theLearnings/Client/learnings-testing.html",ReturningData); 


def options( request,skillof ):
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        return render(request,"theLearnings/Client/skills.html",ReturningData); 



def skills( request,skillof,skill ):
        print('AT HERE')
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        
        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request,skillof,skill) 
        ReturningData['Articals']['CenteredDetails'] = builder.getCenteredDetails(request,skillof,skill) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        return render(request,"theLearnings/Client/skills.html",ReturningData); 



		# path('<str:skillof>/<str:skill>/<str:heading>/<str:subheading>/<str:topic>/',views.showtopic,name='showtopic'), 


def showtopic( request,skillof,skill,heading,subheading,topic ):

        # if request.method == "POST":

        
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)

        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails(request,skillof,skill,heading,subheading,topic) 

        # builder.dummydata_2() 
        way = request.GET.get("task",None)
        if way == "update":
                from .forms import TopicForms
                CenteredDetails = builder.getCenteredDetails(request,skillof,skill,heading,subheading,topic).get("topic")
                # print(">>",CenteredDetails)
                # print(">>",TopicForms(instance=CenteredDetails))
                ReturningData["forms"] = TopicForms(instance=CenteredDetails)
                return render(request,"theLearnings/Client/skills-update.html",ReturningData); 
        elif way == "delete":
                pass
        else:
                pass
        
        ReturningData['Articals']['CenteredDetails'] = builder.getCenteredDetails(request,skillof,skill,heading,subheading,topic) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        # print(ReturningData)
        # print(ReturningData['Articals']['CenteredDetails'])
        return render(request,"theLearnings/Client/skills.html",ReturningData); 




def editTopic( request,skillof,skill,heading,subheading,topic ):
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)

        ReturningData['Articals'] = dict()
        ReturningData['Articals']['Scrollbar'] = builder.getScrollbarDetails(request) 
        ReturningData['Articals']['SidebarLeft'] = builder.getSidebarLeftDetails_forApp(request) 
        ReturningData['Articals']['RelatedArticalsList'] = builder.getRelatedArticalsList(request) 
        ReturningData["forms"] = TopicForms()
        return render(request,"theLearnings/Client/edit-data.html",ReturningData); 









def showlogo(request):
        ReturningData = dict()
        return render(request,"theLearnings/Client/show-logo.html",ReturningData); 




def resting(request):
        ReturningData = dict()
        return render(request,"theLearnings/Client/_resting.html",ReturningData); 




# def handler404(request,exception):
def handler404(request,exception,*args, **kwargs):
        print("at redirection center !!!")
        print(*args,**kwargs)
        # print(args,kwargs)
        # ReturningData = dict()
        # return render(request,"_404.html",status=404); 
        return redirect('/fast404/')



# def fast404(request,*args, **kwargs):
def fast404(request):
        print("at serve template !!! ")
        # print(*args, **kwargs)
        # print(args, kwargs)
        ReturningData = dict()
        ReturningData['previousURL'] = request.META.get('HTTP_REFERER')
        print(ReturningData)
        return render(request,"_404.html",ReturningData); 
        # return redirect('/fast404/')

