


from Home.models import *

class Return:

        def __init__(self,*args,**kwargs):
                self.status = kwargs.get('status',None)             # fail, pass
                self.showtype = kwargs.get('showtype',None)     # success, error, warning, info
                self.message = kwargs.get('message',None)       # "..."
                self.returned = kwargs.get('returned',None)       # object

        def addStatus(self,given):
                self.status = given
        def addShowType(self,given):
                self.showtype = given
        def addMessage(self,given):
                self.message = given
        def addReturned(self,given):
                self.returned = given
        def add(self,*args):
                self.status, self.message, self.returned = args 
        
        def showStatus(self):
                return self.status
        def showShowType(self):
                return self.showtype
        def showMessage(self):
                return self.message
        def showReturned(self):
                return self.returned
        def show(self):
                return {
                        'Status' : self.status,
                        'ShowType' : self.showtype,
                        'Message' : self.message,
                        'Returned' : self.returned
                }
        
        def print(self):
                for key,value in self.show().items():
                        print( f"{key} : {value}" )
                




def ReturningDatabase(request,ReturningData):
        user = request.session.get('user',None) 
        if user and user.get('username',None):
                username = user.get('username',None)
                ReturningData['ObjectUSER'] = USER.objects.get(Username=username)
        # return ReturningData






