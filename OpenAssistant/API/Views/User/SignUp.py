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




'''

Requirements:





ReturnObject = SignUp(
        firstname = ".....",
        lastname = ".....",
        fullname = ".....",
        username = ".....",
        email = ".....",
        mobilenumber = ".....",
        passsword = ".....",
        profile = ".....",
        checked = ".....",
        active = ".....",
)

ReturnObject = SignUp(
        firstname = "SHivam",
        lastname = "SHukla",
        username = "theshivashu",
        email = "theshivashu@gmail.com",
        mobilenumber = "7898565074",
        password = "12345",
        passwordagain = "1234",
        # profile = ".....",
        checked = True,
        # active = ".....",
)



It gives us a 'Return' class object, who gave response like,

ReturnObject = <API.Views.User.Return.Return object at 0x0000022CA2F9D6F0>

>> ReturnObject.status
"pass"
>> ReturnObject.showtype
"success"
>> ReturnObject.message
None
>> ReturnObject.returned
<USER:  user@theshivashu  ( SHivam SHukla ).>

>> ReturnObject.show()
{  'Status' : "pass", 'ShowType' : "success", 'Message' : "User SignUp Successfully !!!", 'Returned' : <USER:  user@theshivashu  ( SHivam SHukla ).>  }

>> ReturnObject.print()
Status : pass
ShowType : success
Message : None
Returned : <USER:  user@theshivashu  ( SHivam SHukla ).>



'''









# def SignUp(*args,**kwargs):
class SignUp:

        def __init__(self, *args, **kwargs):
                object = self.__checks(kwargs)
                if object.status=='pass':
                        object = self.__run(kwargs)
                return object

        def __checks(self,kwargs):

		# if you entered atleast (email or mobilenumber) and password, then you able to signup !!!
                if ( kwargs.get('email',False) or kwargs.get('mobilenumber',False) ) and kwargs.get('password',False):
                        return Return(
				status = 'fail',
                                showtype = 'warning', # success, error, warning, info
				message = "Email or Mobile Number and Password is must to entered !!!",
                        )
		# if passwords are empty or they not matched, so go back to your 'signup' page !!! 
                if kwargs['password']=='' or kwargs['password']!=kwargs['passwordagain']:
                        return Return(
				status = 'fail',
                                showtype = 'warning', # success, error, warning, info
				message = "Password are not matched each other !!!"
			)
		# if user already exist, then go back to your 'signup' page again !!! 
                user = USER.objects.filter(Username=kwargs['username'])
                if user.exists():
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



        def __run(self,kwargs):
                
                try:
                        object = USER()
                        
                        if kwargs['firstname'] and kwargs['lastname']:
                                object.FullName = kwargs.firstname+' '+kwargs['lastname']
                        elif kwargs['firstname']:
                                object.FullName = kwargs['firstname']
                        elif kwargs['lastname']:
                                object.FullName = kwargs['lastname']

                        if kwargs['firstname']:
                                object.FirstName = kwargs['firstname']
                        if kwargs['lastname']:
                                object.LastName = kwargs['lastname']

                        if kwargs['username']:
                                object.Username = kwargs['username']
                        if kwargs['mobilenumber']:
                                object.MobileNumber = kwargs['mobilenumber']
                        if kwargs['email']:
                                object.Email = kwargs['email']
                        if kwargs['password']:
                                object.Password = kwargs['password']
                        if kwargs['profile']:
                                object.Profile = kwargs['profile']
                                
                        if kwargs['checked']:
                                object.isChecked = kwargs['checked']
                        
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
                
                except:
                        return Return(
				status = 'fail',
                                showtype = 'error', # success, error, warning, info
				message = "This error coming from insertion data to model !!!"
			)











