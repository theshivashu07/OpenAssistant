from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

# from django.contrib.auth.models import User

# from django.contrib.auth import authenticate as Authenticate 
# from django.contrib.auth import login as Login
# from django.contrib.auth import logout as Logout
from django.contrib.auth.decorators import login_required as LoginRequired
from API.Code.Management.Sessions import Authenticate, Login, Logout, UserExists


from django.contrib import messages
from Home.models import *
# from theArticals.models import *


from API.Code.User.Return import Return
import API.Code.User.Checks as Checks









# def Logout(*args,**kwargs):
class __Logout:

        def __init__(self, request, *args, **kwargs):
                self.args, self.kwargs = args, kwargs
                self.request = request
                object = self.__checks()
                if object.status=='pass':
                        object = self.__run()
                self.returned = object
                # return object




        def __checks(self):

                # here is we get our logged-in user !!!
                user = UserExists(self.request)

		# if user already not exist, then go back to your 'login' page !!! 
                users = USER.objects.filter(Username=user.Username) 
                if not users.exists():
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "User not exists !!!"
                        ) 
                # if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
                if user is None: 
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "No user LogIn now !!!"
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
                        
                        # .....

                        # this is the edge case - directly working 
                        user = UserExists(self.request)
                        if user:
                                user.isActive = False
                                user.save()

                        # by default add activity on Activities Database
                        action = Actions.objects.get(pk=3) # or name=Logout
                        object = Activities()
                        object.user = user
                        object.action = action
                        object.save()
                        
                        # this is the main process to logged-out
                        Logout(self.request)

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












