from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from Home.models import *

from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired 
from API.Code.User.Return import ReturningDatabase


# def index(request):
# 	return HttpResponse("Hey there, This is <b>User</b>  ( from Client App ) !!!");



@LoginRequired(login_url="/security/login/")
def index(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/index.html",ReturningData); 

# def index(request): 
# 	if not request.user.is_authenticated:
# 		return redirect("security/") 
# 	return render(request,"client/index.html"); 



videos = [
        "https://www.youtube.com/embed/C-9dqfXENb4?si=pvQ2QU1IgOC4itQd",
        "https://www.youtube.com/embed/6_0yhsWCWpQ?si=MwWeqICLJ5a7O2Xl",
        "https://www.youtube.com/embed/mr7uP20YVRg?si=AnyIj5swgH6DnWSu",
        "https://www.youtube.com/embed/tb9-MMstDcg?si=YnLQ4LU6mHQW7PaJ",
        "https://www.youtube.com/embed/6pT_ooV_riQ?si=JPX0jirIFpXhdVs_",
        "https://www.youtube.com/embed/gkiTWVDauV0?si=lwspryXFReyMdrT4",
        "https://www.youtube.com/embed/JG7zBSWWo2E?si=G95EC4_m29nUaADN",
        "https://www.youtube.com/embed/LvdmCPe7I-o?si=XO94adV0-kyguHw_",
        "https://www.youtube.com/embed/IrgOlrVT-mo?si=rxByciyAdc8_rqNZ",
        "https://www.youtube.com/embed/-7VeQh1MnQ0?si=DBfOSGHdQjHasLv6",
        "https://www.youtube.com/embed/ZH2PQ6n-Esc?si=WGEZO_qnSoIGt_UO",
        "https://www.youtube.com/embed/83s2oeJMl94?si=hp35VC47D8DcB5Ns",
        "https://www.youtube.com/embed/NDUPymw7bjg?si=tbCsE2uVMr0YbM7w",
        "https://www.youtube.com/embed/81uTuTaDGKM?si=7gq7wqbc8XBJtaSl",
        "https://www.youtube.com/embed/lVjooGXzGSQ?si=sJCLn7KNt0xO4_Dz",
        "https://www.youtube.com/embed/11Ut-DhIHE4?si=7rLA-NGqcg_KPeIw",
        "https://www.youtube.com/embed/bGVVxFO01Ks?si=080b1WtvQlWk9ucc",
        "https://www.youtube.com/embed/S7kgE68skC8?si=kIn4qK4v55B3oStJ",
        # "https://www.youtube.com/embed/TmB_m40Iwgk?si=CEo1mYUJqtn90YOR",
        # "https",
        # "https",
        # "https",
        # "https",
        # "https",
]




class Menus:
        def __init__(self,dictionary):
                self.name = dictionary.get('name',None)
                self.path = dictionary.get('path',None)
                self.logo = dictionary.get('logo',None)
                # print( self.name, self.path, self.logo )
        def __str__(self):
                return f"<object:Menus | name:{self.name}, url:{self.url}, logo:{self.logo}.>"

l = dict()

sidebar_menus = {
        'Mains' : {
                'Home' : { 'name' : 'Home', 'path' : '/youtube/', 'logo' : 'fa-solid fa-house'},  
                'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                'Subscription' : { 'name' : 'Subscription', 'path' : '/youtube/subscription/', 'logo' : 'fa-solid fa-video'},  
        },
        'Others' : {
                'Accessories' : { 'name' : 'Accessories', 'path' : '/youtube/accessories/', 'logo' : 'fa-solid fa-cart-shopping'},  
                'Spiritual' : { 'name' : 'Spiritual', 'path' : '/youtube/spiritual/', 'logo' : 'fa-solid fa-om'},  
                'Study Learning' : { 'name' : 'Study Learning', 'path' : '/youtube/studylearning/', 'logo' : 'fa-solid fa-book'},  
                'Songs' : { 'name' : 'Songs', 'path' : '/youtube/songs/', 'logo' : 'fa-solid fa-headphones'},  
                'Workout' : { 'name' : 'Workout', 'path' : '/youtube/workout/', 'logo' : 'fa-solid fa-dumbbell'},  
                'Political' : { 'name' : 'Political', 'path' : '/youtube/political/', 'logo' : 'fa-solid fa-landmark-dome'},  
                'Standups' : { 'name' : 'Standups', 'path' : '/youtube/standups/', 'logo' : 'fa-regular fa-face-smile'},  
                'NEWS' : { 'name' : 'NEWS', 'path' : '/youtube/news/', 'logo' : 'fa-solid fa-tv'},  
                'Goods Workspace' : { 'name' : 'Goods Workspace', 'path' : '/youtube/goodsworkspace/', 'logo' : 'fa-regular fa-handshake'},  
                'Announcements' : { 'name' : 'Announcements', 'path' : '/youtube/announcements/', 'logo' : 'fa-solid fa-bullhorn'},  
                'Interview | Podcast' : { 'name' : 'Interview | Podcast', 'path' : '/youtube/intervieworpodcast/', 'logo' : 'fa-solid fa-chalkboard-user'},  
                'Interviews Guide' : { 'name' : 'Interviews Guide', 'path' : '/youtube/interviewsguide/', 'logo' : 'fa-solid fa-person-chalkboard'},  
                'Coding' : { 'name' : 'Coding', 'path' : '/youtube/coding/', 'logo' : 'fa-solid fa-laptop-code'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
        },
}

def getSidebarData():

        Database = dict()
        for keys,values in sidebar_menus.items():
                Database[keys] = dict()
                for key,value in values.items():
                        Database[keys][key] = Menus(
                                dictionary = value
                        )
        # print(Database)
        return Database







@LoginRequired(login_url="/security/login/")
def articals(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/articals.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def problems(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/problems.html",ReturningData); 
        # return render(request,"client/problems-testing.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def youtube(request): 
        ReturningData = dict()

        ReturningData['videos'] = list()
        temp = list()
        limit = 4
        for links in videos:
                temp.append(links)
                if len(temp)==limit:
                        ReturningData['videos'].append(temp)
                        temp = list()
        if temp:
                ReturningData['videos'].append(temp)
                temp = list()
        # print(ReturningData['videos'])

        ReturningData['sidebar'] = getSidebarData()

        ReturningDatabase(request,ReturningData)
        return render(request,"client/youtube.html",ReturningData); 
        # return render(request,"client/youtube-testing.html",ReturningData); 



def youtube_from_(request,from_): 
        ReturningData = dict()

        ReturningData['videos'] = list()
        temp = list()
        limit = 4
        for links in videos:
                temp.append(links)
                if len(temp)==limit:
                        ReturningData['videos'].append(temp)
                        temp = list()
        if temp:
                ReturningData['videos'].append(temp)
                temp = list()
        # print(ReturningData['videos'])

        ReturningData['sidebar'] = getSidebarData()

        ReturningDatabase(request,ReturningData)
        return render(request,"client/youtube.html",ReturningData); 
        # return render(request,"client/youtube-testing.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def hireus(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        print(request.session.get('User',None))
        for keys,values in request.session.items():
                print(f"{keys} : {values}")
        return render(request,"client/hireus.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def notifications(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/notifications.html",ReturningData); 






@LoginRequired(login_url="/security/login/")
def profile(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/profile.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def profile_edit(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/profile_edit.html",ReturningData); 













