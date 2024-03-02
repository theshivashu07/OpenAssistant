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









        # dummydatasubmission_home()
        # dummydatasubmission_articals()
        # dummydatasubmission_articals_new()
        # dummydatasubmission_articals_resubmit()


def dummydatasubmission_home():
        ''' Articals All Database Sets to RUN '''

        listing = [ 'SignUp', 'LogIn', 'Logout', 'Rejoin', 'Temporary Delete', 'Permanent Delete' ] 
        for string in listing: 
                object = Actions() 
                object.name = string 
                object.save() 



def dummydatasubmission_articals():
        ''' Articals All Database Sets to RUN '''

        listing = [ 'Tag', 'Feature' ] 
        for string in listing: 
                object = ContentFrom() 
                object.names = string 
                object.save() 

        contentfrom = ContentFrom.objects.get(pk=1)
        listing = [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', ]
        for string in listing:
                object = ContentOf()
                object.froms = contentfrom
                object.names = string
                object.locations = f"{string}.html"
                object.save()

        contentfrom = ContentFrom.objects.get(pk=2)
        listing = [ 'div', 'table', 'ul' ]
        for string in listing:
                object = ContentOf()
                object.froms = contentfrom
                object.names = string
                object.locations = f"{string}.html"
                object.save()

        print(" Data is saved !!! ")







def dummydatasubmission_articals_new():
        ''' Articals All Database Sets to RUN '''
        # contentfrom = ContentFrom.objects.get(pk=1)
        listing = [ 
                "Introduction, History of Python?",
                "Why we use Python?",
                "Which componies use Python?",
                "Python Setup - Download and Installation.",
                "Is Python a most popular?",
                "Introduction of Django ( Rest Framework ).",
                "How to Python and Django interconnected.",
                "Django's Authentication & Autherization.",
                "How to connect Database with Django.",
                "Python vs C vs C++ vs Java vs Javascript.",
                "Tech with Python (Software,Web,AI,ML).",
         ]
        for string in listing:
                object = Articals()
                object.title = string
                object.save()




def dummydatasubmission_articals_resubmit():
        objects = Articals.objects.all()
        user = USER.objects.get( pk=1 ) 
        for object in objects:
                object.USER = user
                object.save()






