

from theLearnings.models import Skill, SkillOf
from Home.models import OptionsOf,OptionsGroup,Options

# from Home.models import *
from theArticals.models import *
from theArticals.functions.getSidebarRight import getDay,getDate,getAgo


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
        # print(dicting)
        return dicting



'''

from theLearnings.models import Topic,TopicHeadings,TopicSubHeadings
def getSidebarLeftDetails_Skills( request,skillof,skill ): 
        dicting = dict() 
        topics = Topic.objects.filter( skill = Skill.objects.get( slug=skill )  ) 
        # print(topics) 

        for topic in topics: 
                headings = dicting.get( topic.headings.name, dict() ) 
                subheadings = headings.get( topic.subheadings.name, list() ) 
                subheadings.append( { 
                        'name' : topic.title, 
                        'path' : '/learnings/'+skillof+'/'+skill+'/'+topic.headings.slug+'/'+topic.subheadings.slug+'/'+topic.slug+'/' 
                } ) 

                headings[ topic.subheadings.name ] = subheadings 
                dicting[ topic.headings.name ] = headings 
                
        return dicting 

'''


from theLearnings.models import Topic,TopicHeadings,TopicSubHeadings
def getSidebarLeftDetails( request,skillof,skill,heading=None,subheading=None,topic=None): 
        dicting = dict() 
        topics = Topic.objects.filter( skill = Skill.objects.get( slug=skill )  ) 
        for topic_ in topics: 
                headings = dicting.get( topic_.headings.name, dict() ) 
                subheadings = headings.get( topic_.subheadings.name, dict() ) 
                data = { 
                        'name' : topic_.title, 
                        'path' : '/learnings/'+skillof+'/'+skill+'/'+topic_.headings.slug+'/'+topic_.subheadings.slug+'/'+topic_.slug+'/',
                }
                
                subheadings[ topic_.title ] = data 
                subheadings[  'securedslugOfSubheading' ] = topic_.subheadings.slug  

                headings[ topic_.subheadings.name ] = subheadings 
                headings[  'securedslugOfHeading' ] = topic_.headings.slug  

                dicting[ topic_.headings.name ] = headings 
                
        return dicting



def getCenteredDetails( request,skillof,skill,heading=None,subheading=None,topic=None ): 

        # print( "BEFORE :  ",skillof,skill,heading,subheading,topic )

        skill = Skill.objects.filter( slug=skill ).first()
        
        if heading: 
                heading = TopicHeadings.objects.filter( skill=skill, slug=heading ).first()
        else:
                heading = TopicHeadings.objects.filter( skill=skill ).first()

        if subheading: 
                subheading = TopicSubHeadings.objects.filter( skill=skill, headings=heading, slug=subheading ).first()
        else:
                subheading = TopicSubHeadings.objects.filter( skill=skill, headings=heading ).first()

        if topic: 
                topic = Topic.objects.filter( skill=skill, headings=heading, subheadings=subheading, slug=topic ).first()
        else:
                topic = Topic.objects.filter( skill=skill, headings=heading, subheadings=subheading ).first()

        # print( "AFTER :  ",skillof,skill,heading,subheading,topic )

        # return topic 
        return {
                "topic" : topic,
                "head" : {
                        "user" : str(topic.USER.FullName),
                        "skill" : skill.name,
                        "heading" : heading.name,
                        "subheading" : subheading.name,
                        "topic" : topic.title,
                        "path" : f"{skill.slug}/{heading.slug}/{subheading.slug}/{topic.slug}", 
                        "date" : getDate(topic.joiningdate),
                        "day" : getDay(topic.joiningdate),
                        "ago" : getAgo(topic.updationdate),
                        # "datetime" : "{} — {} — {}".format( getDate(topic.joiningdate), getDay(topic.joiningdate), getAgo(topic.updationdate) ),
                }
        }





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





















##########################################################################

# DUMMY DATA CENTER #











from theLearnings.models import Topic,TopicHeadings,TopicSubHeadings
def dummydata_1( *args,**kwargs ):
        # basics/datatypes/definitions/
        heading = TopicHeadings.objects.filter( slug='basics' )[0]
        subheading = TopicSubHeadings.objects.filter( headings=heading,slug='datatypes' )[0]
        subheadings = TopicSubHeadings.objects.filter( headings=heading )
        topics = Topic.objects.filter( headings=heading,subheadings=subheading ) 
        for subheading in subheadings: 
                if subheading.slug in [ 'keywords','constants','variables','identifiers','namespaces',
                                       'literals','statement','indentations','comments',  ]:
                        for topic in topics:
                                objects = Topic()
                                objects.USER = topic.USER
                                objects.skill = topic.skill
                                objects.headings = heading
                                objects.subheadings = subheading
                                objects.title = topic.title
                                objects.content = topic.content
                                objects.discription = topic.discription
                                objects.save()
        
        print( "All Sets" )
        return




from theLearnings.models import Topic,TopicHeadings,TopicSubHeadings
def dummydata_2( *args,**kwargs ):
        # basics/datatypes/definitions/
        skill = Skill.objects.filter( name="Python" )[0]

        heading = TopicHeadings.objects.filter( slug='basics' )[0]
        subheading = TopicSubHeadings.objects.filter( headings=heading,slug='datatypes' )[0]
        # topics = Topic.objects.filter( headings=heading,subheadings=subheading ) 
        topics = Topic.objects.all() 
        for topic in topics: 
                if not topic.skill:
                        # print(topic.title)
                        topic.skill = skill
                        topic.save()
        
        # print( "All Sets" )
        return




















