import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

# from django.contrib.auth import authenticate as Authenticate
# from django.contrib.auth import login as Login
# from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required as LoginRequired
from API.Code.Management.Sessions import Authenticate, Login, Logout

from django.contrib import messages
from .models import *


import API.Code.User.LogIn as __Logout
import API.Code.User.LogIn as __LogIn
import API.Code.User.SignUp as __SignUp
import API.Code.User.Return as __Return


import API.Code.Management.Messages as __Messages
import API.Code.Management.Sessions as __Sessions


# def index(request):
# 	return HttpResponse("Hey there, This is <b>Client</b>  ( from Home App ) !!!");


@LoginRequired(login_url="/security/login/")
def askedquestions(request):
	return render(request,"home/asked-questions.html"); 
	# return redirect("/security/asked-questions/")


def index(request): 
	# if we first time come here, and there is no user registered, then redirect that to 'signup' page...
	if USER.objects.all():
		return redirect("/security/login/"); 
	else:
		return redirect("/security/signup/")
	# return redirect("/security/login/"); 




# if value is blank string or None return None, otherwise return original string...
# this function is needed in everypoint of getting values back to the work...
def filterValue(value):
          if value:
                    return value
          return None

def signup(request): 

	# it will required for all, don't worry about method...
	ReturningData = dict() 

	if request.method == "POST":

		SignUpObject = __SignUp.__SignUp(
			request = request,
			firstname = filterValue(request.POST.get('firstname',None)),
			lastname = filterValue(request.POST.get('lastname',None)),
			username = filterValue(request.POST.get('username',None)),
			email = filterValue(request.POST.get('email',None)),
			mobile = filterValue(request.POST.get('mobile',None)),
			password = filterValue(request.POST.get('password',None)),
			passwordagain = filterValue(request.POST.get('passwordagain',None)),
			profile = filterValue(request.POST.get('profile',None)),
			check = filterValue(request.POST.get('check',None)),
			# active = filterValue(request.POST.get('active',None)),
		)

		ReturnObject = SignUpObject.returned 

		__Messages.__Messages(
			request = request, 
			ReturnObject = ReturnObject,
		)

		if ReturnObject.status == "pass":
			__Sessions.SignInSessions(
				request = request,
				ReturnObject = ReturnObject,
			)
			return redirect("/security/login/")

		# elif ReturnObject.status == "fail":
		ReturningData = {
			'values' : {
				'firstname' : request.POST.get('firstname',None),
				'lastname' : request.POST.get('lastname',None),
				'mobile' : request.POST.get('mobile',None),
				'email' : request.POST.get('email',None),
				'username' : request.POST.get('username',None),
				'password' : request.POST.get('password',None),
				'passwordagain' : request.POST.get('passwordagain',None),
				# 'profile' : request.POST.get('profile',None),
				'check' : request.POST.get('check',None),
				# 'active' : request.POST.get('active',None),	
			}
		}
		return render(request,"home/signup.html", ReturningData); 

	return render(request,"home/signup.html", ReturningData); 





def login(request): 

	# print( request.session )
	# print( request.session.get('username' ) )

	if request.method == "POST":
		next = filterValue(request.POST.get('next',None))
		print('NEXT :',next)
		LogInObject = __LogIn.__LogIn(
			request = request,
			user = filterValue(request.POST.get('user',None)),
			by = filterValue(request.POST.get('by',None)),
			password = filterValue(request.POST.get('password',None)),
			check = filterValue(request.POST.get('check',None)),
		)

		ReturnObject = LogInObject.returned 

		__Messages.__Messages( 
			request = request, 
			ReturnObject = ReturnObject, 
		) 

		if ReturnObject.status == "pass":
			__Sessions.LogInSessions( 
				request = request, 
				ReturnObject = ReturnObject, 
			) 

			# if this login comes 
			print("NEXT :",next)
			if next not in [ '', None ]:
				return redirect(next)
			return redirect("/") 
		
		# elif ReturnObject.status == "fail":
		ReturningData = {
			'values' : {
				'user' : filterValue(request.POST.get('user',None)),
				'by' : filterValue(request.POST.get('by',None)),
				'password' : filterValue(request.POST.get('password',None)),
				'check' : filterValue(request.POST.get('check',None)),
			},
		}
		
		return render(request,"home/login.html", ReturningData); 

	ReturningData = dict()
	currUrlPath = request.build_absolute_uri() 
	prevUrlPath = request.META.get('HTTP_REFERER') 
	# we check if current login path is not equal to previous path, means we are able to show username and password 
	if currUrlPath != prevUrlPath: 
		for user in USER.objects.all()[::-1]: 
			if user.isChecked: 
				values = {
					'user' : user.Username,
					'by' : 'username',
					'password' : user.Password,
					'check' : user.isChecked,
				}
				ReturningData['values'] = values
				break 
	return render(request,"home/login.html", ReturningData); 

def logout(request): 
	ReturningData = dict() 
	return render(request,"home/logout.html", ReturningData); 

def resetpassword(request): 
	ReturningData = dict() 
	return render(request,"home/resetpassword.html", ReturningData); 

# def askedquestions(request):
# 	ReturningData = dict()
# 	return render(request,"home/askedquestions.html", ReturningData); 

def userslist(request):
	ReturningData = dict()
	return render(request,"home/users-list.html", ReturningData); 

def defaultuser(request):
	ReturningData = dict()
	return render(request,"home/defaultuser.html", ReturningData); 

# def defaultuser(request):
# 	ReturningData = dict()
# 	return render(request,"home/defaultuser.html", ReturningData); 







