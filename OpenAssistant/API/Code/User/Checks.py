
# from django.contrib.auth import authenticate as Authenticate
from API.Code.Management.Sessions import Authenticate, Login, Logout


from Home.models import *





class SignUpChecks:

        def MustFieldAvailable(self,email,mobilenumber,password):
                if email and password:
                        return True
                elif mobilenumber and password:
                        return True
                #else : and now return for any conditions...
                return False 
        
        def PasswordsMatches(self,password,passwordagain):
                if password in [ '', None ]:
                        return False
                elif password==passwordagain:
                        return True
                #else : and now return for any conditions...
                return False
        
        def UsernameExist(self,username):
                user = USER.objects.filter(Username=username )
                if user.exists():
                        return True
                #else : and now return for any conditions...
                return False





class LogInChecks:

        def UsernameExist(self,username):
                    user = USER.objects.filter(Username=username) 
                    if user.exists():
                            return True
                    return False 
        
        def UserAuthenticated(self,username,password):
                print(username,password)
                userauth = Authenticate(username=username, password=password)
                if userauth:
                        return True 
                return False 
                '''
                    # userauth = Authenticate(username=username, password=password)
                    user = USER.objects.get(Username=username)
                    # if userauth is None:
                    if user.Password == password:
                              return True 
                    return False 
                '''

'''
                    # userauth = Authenticate(username=username, password=password)
                    user = USER.objects.filter(Username=username, Password=password)
                    # if userauth is None:
                    if user.exists():
                              return True 
                    return False 
'''