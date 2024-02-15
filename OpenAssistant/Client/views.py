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
        "https://www.youtube.com/embed/TmB_m40Iwgk?si=CEo1mYUJqtn90YOR",
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
        # "https",
        # "https",
        # "https",
        # "https",
        # "https",
]




@LoginRequired(login_url="/security/login/")
def articals(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/articals.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def problems(request): 
        ReturningData = dict()
        ReturningDatabase(request,ReturningData)
        return render(request,"client/problems-testing.html",ReturningData); 
        return render(request,"client/problems.html",ReturningData); 


@LoginRequired(login_url="/security/login/")
def youtube(request): 
        ReturningData = dict()

        ReturningData['videos'] = list()
        temp = list()
        limit = 3
        for links in videos:
                temp.append(links)
                if len(temp)==limit:
                        ReturningData['videos'].append(temp)
                        temp = list()
        if temp:
                ReturningData['videos'].append(temp)
                temp = list()
        # print(ReturningData['videos'])

        ReturningDatabase(request,ReturningData)
        return render(request,"client/youtube-testing.html",ReturningData); 
        return render(request,"client/youtube.html",ReturningData); 


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













