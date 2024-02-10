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











        


# def SignUp(*args,**kwargs):
class __SignUp:

        def __init__(self,*args,**kwargs):
                self.args, self.kwargs = args, kwargs
                self.request = self.__getValueOfKey('request')
                
                object = self.__checks()
                if object.status=='pass':
                        object = self.__run()
                self.returned = object
                #return object 

        def __getValueOfKey(self,key,otherwise=None):
              return self.kwargs.get(key,otherwise)

        def __checks(self,*args,**kwargs):
                ''' there is no use or *args, **kwargs, but to play save i use this, may in future we pass something...'''

                checks = Checks.SignUpChecks()

                # if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
                if not checks.MustFieldAvailable( self.__getValueOfKey('email'), self.__getValueOfKey('mobilenumber'), self.__getValueOfKey('password') ):
                        return Return(
                                status = 'fail',
                                showtype = 'warning', # success, error, warning, info
                                message = "Email or Mobile Number and Password is must to entered !!!",
                        )
                # if passwords are empty or they not matched, so go back to your 'signup' page !!! 
                if not checks.PasswordsMatches( self.__getValueOfKey('password'), self.__getValueOfKey('passwordagain') ):
                        return Return(
                                status = 'fail',
                                showtype = 'warning', # success, error, warning, info
                                message = "Password are not matched each other !!!"
                        )
                # if user already exist, then go back to your 'signup' page again !!!
                if checks.UsernameExist( self.__getValueOfKey('username') ):
                        return Return(
                                status = 'fail',
                                showtype = 'info', # success, error, warning, info
                                message = "User already exists !!!"
                        )

                # default returning content, if everything okay !!!
                return Return(
                        status = 'pass',
                        showtype = 'success', # success, error, warning, info
                        message = "Good to go chief !!!"
                )



        def __run(self,*args,**kwargs):
                ''' there is no use or *args, **kwargs, but to play save i use this, may in future we pass something...'''
                
                try:
                        object = USER()

                        if self.__getValueOfKey('firstname') and self.__getValueOfKey('lastname'):
                                object.FullName = self.__getValueOfKey('firstname') + ' ' + self.__getValueOfKey('lastname')
                        elif self.__getValueOfKey('firstname'):
                                object.FullName = self.__getValueOfKey('firstname')
                        elif self.__getValueOfKey('lastname'):
                                object.FullName = self.__getValueOfKey('lastname')

                        if self.__getValueOfKey('firstname'):
                                object.FirstName = self.__getValueOfKey('firstname')
                        if self.__getValueOfKey('lastname'):
                                object.LastName = self.__getValueOfKey('lastname')

                        if self.__getValueOfKey('username'):
                                object.Username = self.__getValueOfKey('username')
                        if self.__getValueOfKey('mobile'):
                                object.Mobile = self.__getValueOfKey('mobile')
                        if self.__getValueOfKey('email'):
                                object.Email = self.__getValueOfKey('email')
                        if self.__getValueOfKey('password'):
                                object.Password = self.__getValueOfKey('password')
                        if self.__getValueOfKey('profile'):
                                object.Profile = self.__getValueOfKey('profile')
                        if self.__getValueOfKey('check'):
                                object.isChecked = bool(self.__getValueOfKey('check',False))
                        object.isActive = False
                        object.save()
                        
                        # Also submit data to Activity model...
                        activityObject = Activities(
                                user = object,
                                action = Actions.objects.get(pk=1) 
                        )
                        
                        return Return(
                            status = 'pass',
                            showtype = 'success', # success, error, warning, info
                            message = "User SignUp Successfully !!!",
                            returned = object,
                        )
                
                # except:
                except Exception as e:
                        return Return(
                            status = 'fail',
                            showtype = 'error', # success, error, warning, info
                            message = "This error coming from insertion data to model !!!" + e,
                        )










