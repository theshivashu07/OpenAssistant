
from django.contrib.auth import authenticate as Authenticate



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

        def UserExist(self,username):
                    user = USER.objects.filter(Username=username) 
                    if user.exists():
                            return True
                    return False 
        
        def UserAuthenticated(self,username,password):
                    userauth = Authenticate(username=username, password=password)
                    # if userauth is None:
                    if userauth:
                              return True 
                    return False 

