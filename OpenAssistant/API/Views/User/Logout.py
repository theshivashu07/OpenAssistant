from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.models import User

from django.contrib.auth import authenticate as Authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required as LoginRequired

from django.contrib import messages
from Home.models import *

from API.Views.User.Return import *










# def Logout(*args,**kwargs):
class Logout:

        def __init__(self, request, *args, **kwargs):
                object = self.__checks(kwargs)
                if object.status=='pass':
                        object = self.__run(request,kwargs)
                return object




        def __checks(self,kwargs):

		# if user already not exist, then go back to your 'login' page !!! 
                user = USER.objects.filter(Username=kwargs.username) 
                if not user.exists():
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "User not exists !!!"
                        )
                userauth = Authenticate(username=kwargs.username, password=kwargs.password)
                # if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
                if userauth is None:
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "Invalid User, username and password not matched !!!"
                        )
                
		# default returning content, if everything okay !!!
                return Return(
		        status = 'pass',
                        showtype = 'success', # success, error, warning, info
			message = "Good to go chief !!!",
			# returned = userauth,
                )



        def __run(self,request,kwargs):
                
                try:
                        
                        # .....

                        return Return(
				status = 'pass',
                                showtype = 'success', # success, error, warning, info
				message = "User LogIn Successfully !!!",
                                returned = object,
                        )


                except:
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "This error coming from insertion data to model !!!"
			)












