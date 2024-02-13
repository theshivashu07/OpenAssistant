

from Home.models import *
from django.shortcuts import render,redirect




def Login(request,username):
        request.session['user'] = {
                'username' : username, 
                'status' : True
	}
        print("Login Done :",request.session.get('user',None)) 

def Logout(request):
        request.session['deleted_user'] = request.session['user'] 
        del request.session['user']
        print("Logout Done :",request.session.get('user',None)) 

def Authenticate(username,password):
        users = USER.objects.filter(Username=username,Password=password)
        print("Authentication Done :",users.exists())
        if users.exists():
                return users[0]
        return False

# that is decorator and the arguments you pass on it, all these are same like normal function...
def LoginRequired( function=None, login_url=None ):
        # and on that function, which argument we mention here, those are the original function, which we want to call...
        def inner( askedquestions ):
                # and mentioned arguments are those who we pass when we call to original function
                def wrapper(request,default=None):

                        # from django.core.management.commands.runserver import Command as runserver
                        # address = runserver.default_addr
                        # port = runserver.default_port
                        # next = request.path

                        path = f"{login_url}?next={request.path}" 
                        if request.session.get('user',None): 
                                return askedquestions(request)
                        else: 
                                return redirect(path) 
                        

                return wrapper 
        return inner 


# def getpaths(request,login_url="/security/login/"): 
# 	# http://localhost:1234/security/users-list/
# 	# http://localhost:1234/security/login/?next=/security/asked-questions/
# 	from django.core.management.commands.runserver import Command as runserver  

# 	address = runserver.default_addr
# 	port = runserver.default_port
# 	next = request.path
# 	print( f" address : '{address}', port : '{port}', next : '{next}' " )

# 	# path = f"{basepath}/{login_url}/?next={request.path}/"
# 	path = f"http://{address}:{port}{login_url}?next={next}asked-questions/"
# 	# path = f"http://{address}:{port}{login_url}/?next={next}"
# 	print(path)

# getpaths(request)


class SignInSessions:

          def __init__(self,request,ReturnObject):
                  self.request ,self.ReturnObject= request,ReturnObject.returned 
                  self.__sessions()

          def __sessions(self):
                  return None






class LogInSessions:

          def __init__(self,request,ReturnObject):
                  self.request ,self.ReturnObject= request,ReturnObject.returned 
                  self.__sessions()

          def __sessions(self):
                    self.request.session['user'] = {
			'username' : self.ReturnObject.Username, 
		}
                  



















