
from Home.models import USER
from theArticals.models import Articals



def getUser(request):
          ''' if user logged-in return User's Object, otherwise return 'None' '''
          user = request.session.get('user',None)
          if user:
                    user = user['username'] 
                    user = USER.objects.get(Username=user)
          return user 

def getArtical(request,slug):
        ''' opened '''
        slug = slug if slug else request.GET.get('slug',None) 
        artical = request.GET.get('artical',None) 
        if artical:
                artical = Articals.objects.filter( slug=slug )[0] 





def getRecentArticalsList(request):   
          ListOfArticals = list() 
          user = getUser(request) 
          if user: 
                    articals = Articals.objects.filter(USER=user) 
                    for artical in articals: 
                              ListOfArticals.append( artical ) 
          return ListOfArticals 



def getOpenedArticalsDetails(request):
                USER = getUser(request) 
                OpenedArtical = dict()
                OpenedArtical['Head'] = {
                        'Title' : None,
                        'Slug' : None,
                        'USER' : {
                                'name' : USER.FullName,
                                'username' : USER.Username,
                                'url' : "/".join([ 'user', USER.Username])
                        },
                }
                OpenedArtical['Content'] = dict()
                dataset = ()
                # for dictionary in ArticalsActivityStore:
                for dictionary in list():
                        pass

          



















