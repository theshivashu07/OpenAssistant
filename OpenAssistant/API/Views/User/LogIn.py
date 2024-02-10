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


from API.Views.User.Return import Return
import API.Views.User.Checks as Checks









# def LogIn(*args,**kwargs):
class LogIn:

        def __init__(self, request, *args, **kwargs):
                self.args, self.kwargs = args, kwargs
                self.request = self.__getValueOfKey('request')
                
                object = self.__checks()
                if object.status=='pass':
                        object = self.__run(request,kwargs)
                self.returned = object
                #return object 

        def __getValueOfKey(self,key,otherwise=None):
              return self.kwargs.get(key,otherwise)


        def __checks(self,kwargs):

                checks = Checks.LogInChecks()

		# if user not exist, then go back to your 'login' page !!! 
                if not checks.UserExist(  self.__getValueOfKey('username') ):
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "User not exists !!!"
                        )
                # if user is authenticated, then we move for next process !!!
                if not checks.UserAuthenticated(  self.__getValueOfKey('username'), self.__getValueOfKey('password') ):
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
                        
                        userauth = Authenticate(username=kwargs.username, password=kwargs.password)
                        Login(request, userauth) 

                        object = USER.objects.get( Username=kwargs.username )
                        if kwargs.checks:
                                object.isChecked = True
                        object.isActive = True
                        object.save()

                        # its time to redirects
                        # if kwargs.next not in [ '', None ]:
                        #         return redirect(kwargs.next)
                        # return redirect("/"); 

                        activityObject = Activities(
                                user = object,
                                action = Actions.objects.get(pk=2) 
                        )

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



















