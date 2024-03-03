from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.models import User

# from django.contrib.auth import authenticate as Authenticate 
# from django.contrib.auth import login as Login
# from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required as LoginRequired
from API.Code.Management.Sessions import Authenticate, Login, Logout

from django.contrib import messages
from Home.models import *
from theArticals.models import *


from API.Code.User.Return import Return
import API.Code.User.Checks as Checks









# def LogIn(*args,**kwargs):
class __LogIn:

        def __init__(self, request, *args, **kwargs):
                self.args, self.kwargs = args, kwargs
                self.request = request
                print(self.request)
                
                object = self.__checks()
                if object.status=='pass':
                        object = self.__run()
                self.returned = object
                #return object 

        def __getValueOfKey(self,key,otherwise=None):
              return self.kwargs.get(key,otherwise)


        def __checks(self):

                checks = Checks.LogInChecks()

		# if user not exist, then go back to your 'login' page !!! 
                if not checks.UsernameExist(  self.__getValueOfKey('user') ):
                        return Return( 
				status = 'fail', 
                                showtype = 'error', # success, error, warning, info 
				message = "User not exists !!!" 
                        )
                # if user is authenticated, then we move for next process !!!
                if not checks.UserAuthenticated(  self.__getValueOfKey('user'), self.__getValueOfKey('password') ):
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



        def __run(self):
                
                try:
                        
                        # userauth = Authenticate(username=self.kwargs.username, password=self.kwargs.password)
                        print(self.__getValueOfKey('user'),self.__getValueOfKey('password'))
                        # user = Authenticate(username=self.__getValueOfKey('user'), password=self.__getValueOfKey('password'))
                        user = USER.objects.get(Username=self.__getValueOfKey('user'), Password=self.__getValueOfKey('password'))
                        print(user)
                        print(self.request, user.Username)
                        Login(self.request, user.Username) 

                        # by default add activity on Activities Database
                        action = Actions.objects.get(pk=2) # or name=LogIn
                        object = Activities()
                        object.user = user
                        object.action = action
                        object.save()

                        object = USER.objects.get( Username=self.__getValueOfKey('user') )
                        if self.__getValueOfKey('checks'):
                                object.isChecked = True
                        object.isActive = True
                        object.save()

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



















