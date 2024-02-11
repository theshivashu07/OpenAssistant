

from Home.models import *




def Login(request,username):
        request.session['user'] = {
                'username' : username, 
                'status' : True
	}
        print("Login Done :",request.session['user'])

def Logout(request):
        del request.session['user']['status']
        print("Logout Done :",request.session['user'])

def Authenticate(username,password):
        users = USER.objects.filter(Username=username,Password=password)
        print("Authentication Done :",users.exists())
        if users.exists():
                return users[0]
        return False
        


                





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
                  



















