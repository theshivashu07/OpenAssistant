

from theLearnings.models import Skill, SkillOf
from Home.models import OptionsOf,OptionsGroup,Options

# from Home.models import *
from theArticals.models import *



def getScrollbarDetails( request ):
          returningdataset = dict()
          skillofs = SkillOf.objects.all()
          for skillof in skillofs:
                  skills = Skill.objects.filter( skillsof=skillof, status=True ) 
                  # skills = Skill.objects.filter( skillsof=skillof ).filter( status=True )  
                  for skill in skills: 
                         returningdataset[skill.name] = { 
                                 'name' : skill.name, 
                                #  'path' : '/learnings/'+skill.slug+'/' 
                                 'path' : '/learnings/'+skill.skillsof.slug+'/'+skill.slug+'/' 
                        } 
                        #  print( returningdataset )  
        #   print( returningdataset )  
          return returningdataset   




def knowoptionsof(request):
        ''' function to know that this URL if coming from this APP '''
        data = {
                '/problems/' : 'Problems',
                '/articals/' : 'Articals',
                '/youtube/' : 'YouTube',
                '/aadhyatm/' : 'Aadhyatm',
                '/hire-us/' : 'Hire US',
                '/profile/' : 'Profile',
                '/learnings/' : 'Learnings',
                # '' : 'Home',
        }
        for key,value in data.items():
                if key in request.path:
                        return value
        return data.get(request.path,'Home') 

def getSidebarLeftDetails(request): 
        ''' this function is to get all Options related to this App '''
        dicting = dict()
        optionsof = OptionsOf.objects.get( name=knowoptionsof(request) )
        optionsgroup_list = OptionsGroup.objects.filter( optionsof=optionsof ) 
        # print(optionsgroup_list)
        for optionsgroup in optionsgroup_list:
                temp = list() 
                options_list = Options.objects.filter( optionsgroup=optionsgroup ) 
                for options in options_list:
                        temp.append( options )
                        # print( options.name )
                dicting[optionsgroup.name] = temp
                # print(temp)
        print(dicting)
        return dicting




from theLearnings.models import Topic,TopicHeadings,TopicSubHeadings
def getSidebarLeftDetails_Skills( request,skillof,skill ): 
        dicting = dict()
        skill = Skill.objects.get( name=skill )
        topics = Topic.objects.filter( skill=skill ) 









def getOptionsDetails( skillof ):
        returningdataset = dict()
        skills = Skill.objects.filter( skillof=skillof )
        for skill in skills:
                returningdataset[skill.name] = {
                        'name' : skill.name, 
                        # 'image' : skill.image,
                        'path' : '/learnings/'+skill.skillsof.slug+'/'+skill.slug+'/' 
                } 
        print( returningdataset )  
        return returningdataset   
        
                


def getUser(request):
          ''' if user logged-in return User's Object, otherwise return 'None' '''
          user = request.session.get('user',None)
          if user:
                    user = user['username'] 
                    user = USER.objects.get(Username=user)
          return user 

def getRelatedArticalsList(request):   
          ListOfArticals = list() 
          user = getUser(request) 
          if user: 
                    articals = Articals.objects.filter(USER=user) 
                    for artical in articals: 
                              ListOfArticals.append( artical ) 
          return ListOfArticals 
























