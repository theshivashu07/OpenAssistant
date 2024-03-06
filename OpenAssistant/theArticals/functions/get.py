
from Home.models import USER
from theArticals.models import Articals
from API.models import Skills,SkillsOf, SkillsGroup, SkillSetsBuild



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

          

###################################################################
                









#-----------------------------------------------------------------------
        

showonly = [ 1,4,5,3, ]
def getScrollbarDetails(request):
        count = 0
        objects = SkillSetsBuild.objects.all()
        sets,lists = set(),list() #
        returningdataset = dict()
        for object in objects:
                if object.skillsof.id in showonly:
                        count +=1
                        if object not in sets:
                                sets.add(object)
                                lists.append(object)
                                returningdataset[object.skills.name] = {
                                        'name' : object.skills.name,
                                        'path' : '/articals/'+object.slug+'/'
                                }
        return returningdataset


def getSkillsets(request):
        objects = SkillSetsBuild.objects.all()
        dataset = list()
        for object in objects:
                data = {
                        'id' : object.skills.id, 
                        'name' : object.skills.name, 
                        'string' : f"{object.skills.name} | {object.skillsgroup.name} | {object.skillsof.name}"
                }
                dataset.append( data )
        return dataset








