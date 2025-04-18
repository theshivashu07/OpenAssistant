import profile
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

# from django.contrib.auth import authenticate as Authenticate
# from django.contrib.auth import login as Login
# from django.contrib.auth import logout as Logout
# from django.contrib.auth.decorators import login_required as LoginRequired
from API.Code.Management.Sessions import Authenticate, Login, Logout, LoginRequired, UserExists
# from django.contrib.auth.decorators import login_required as LoginRequired

from django.contrib import messages
from .models import *


import API.Code.User.Logout as __Logout
import API.Code.User.LogIn as __LogIn
import API.Code.User.SignUp as __SignUp 
import API.Code.User.Return as __Return
from API.Code.User.Return import ReturningDatabase


import API.Code.Management.Messages as __Messages
import API.Code.Management.Sessions as __Sessions







# def index(request):
# 	return HttpResponse("Hey there, This is <b>Client</b>  ( from Home App ) !!!");


@LoginRequired(login_url="/security/login/")
def askedquestions(request):
	ReturningData = {}
	ReturningDatabase(request,ReturningData)
	return render(request,"home/asked-questions.html",ReturningData); 
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

	# if user is already logged in, then redirect to home page...
	# we have two ways of login, so may you login
	# if request.user.is_authenticated:
	# 	Login(request,request.user.username)
	# 	print(f"new user is logged in !!!  {request.user.username}")
	# 	return redirect("/") 
	
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
	
	if request.user.is_authenticated:
		print(dir(request.user))
		print(request.user,request.user.username,request.user.email,request.user.first_name,request.user.last_name,request.user.is_authenticated,request.user.is_active,request.user.is_staff,request.user.is_superuser)
	
	return render(request,"home/login.html", ReturningData); 

def logout(request): 

	LogoutObject = __Logout.__Logout(
		request = request,
		user = filterValue(request.POST.get('user',None)),
		by = filterValue(request.POST.get('by',None)),
		password = filterValue(request.POST.get('password',None)),
		check = filterValue(request.POST.get('check',None)),
	)

	return redirect('/security/login/')
	# ReturningData = dict() 
	# return render(request,"home/logout.html", ReturningData); 



from django.contrib.auth.models import User

def profilesetup(request): 
	print(dir(request.user))

	if request.method == "POST":

		user = request.POST.get('user',None) 
		user = User.objects.filter(Username=user).first()
		
		# if user:
		if user:
			# user.FirstName = request.POST.get('firstname',None)
			# user.LastName = request.POST.get('lastname',None)
			# # user.Mobile = request.POST.get('mobile',None)
			# user.Email = request.POST.get('email',None)
			# user.Username = request.POST.get('username',None)
			user.Password = request.POST.get('password',None)
			# user.PasswordAgain = request.POST.get('passwordagain',None)
			# # user.Profile = request.POST.get('profile',None)
			# # user.isChecked = request.POST.get('check',None)
			# # user.isActive = request.POST.get('active',None)
			# user.save()
			print("User from POST !!!")
			# return redirect("/")
			return signup(request)

	print("User from GET !!!")

	ReturningData = dict() 
	ReturningData['values'] = {
		'firstname' : request.user.first_name,
		'lastname' : request.user.last_name,
		# 'mobile' : request.user.mobile,
		'email' : request.user.email,
		'username' : request.user.username,
		'password' : request.user.password,
		'passwordagain' : request.user.password,
		# 'profile' : request.user.profile,
		# 'check' : request.user.isChecked,
		# 'active' : request.user.isActive,
	}
	return render(request,"home/profile-setup.html", ReturningData); 


def resetpassword(request): 
	ReturningData = dict() 
	return render(request,"home/resetpassword.html", ReturningData); 

# def askedquestions(request):
# 	ReturningData = dict()
# 	return render(request,"home/askedquestions.html", ReturningData); 

def userslist(request):

	ReturningData = dict()

	objects = USER.objects.all() 
	users = list()
	for user in objects:
		users.append( user ) 
	ReturningData['values'] = {
		'userslist' : users,
	}
	ReturningDatabase(request,ReturningData)
	return render(request,"home/users-list.html", ReturningData); 

def defaultuser(request):
	# default()
	ReturningData = dict()
	ReturningDatabase(request,ReturningData)
	return render(request,"home/default-user.html", ReturningData); 



# this function is to submit bulk data, but dont's push the data if you have already, so be carefull and click only once on that link...
# add this function to a defaultuser(), so that data automatically save when you click on logo button, but only once, else overwrite data...
from _dummydatabase.default import submitdummydata 
def default(): 
	print("Working.....",end=" ") 
	submitdummydata() 
	print("Bulk data submitted directly!!!") 


