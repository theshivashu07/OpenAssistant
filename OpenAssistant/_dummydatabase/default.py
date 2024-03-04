


from theArticals.models import *
from Home.models import *
from API.models import *




def submitdummydata(user=None):
          # dummydatasubmission__()
          # return None
          if user:
                    dummydatasubmission_()
          else:
                    dummydatasubmission()
          return



def dummydatasubmission():
        ''' Articals All Database Sets to RUN '''
        ''' Actions(), ContentFrom(), ContentOf(),  '''


        listing = [ 'SignUp', 'LogIn', 'Logout', 'Rejoin', 'Temporary Delete', 'Permanent Delete' ] 
        for string in listing: 
                object = Actions() 
                object.name = string 
                object.save() 

        dicting = { 
                'Tag' : [ 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', ],
                'Feature' : [ 'div', 'table', 'ul' ],
        } 
        for key,values in dicting.items(): 
                object = ContentFrom() 
                object.names = key 
                object.save() 
                contentfrom=object
                for string in values: 
                        object = ContentOf()
                        object.froms = contentfrom
                        object.names = string
                        object.locations = f"{string}.html"
                        object.save()
                
        print(" Data is saved !!! ")


def dummydatasubmission_():
        ''' Articals All Database Sets to RUN - After Any one user loggedin'''
        # ''' Actions(), ContentFrom(), ContentOf(),  '''
        ''' Articals() '''

        listing = [ 
                "Introduction, History of Python?",
                "Why we use Python?",
                "Which componies use Python?",
                "Python Setup - Download and Installation.",
                "Is Python a most popular?",
                "Introduction of Django ( Rest Framework ).",
                "How to Python and Django interconnected.",
                "Django's Authentication & Autherization.",
                "How to connect Database with Django.",
                "Python vs C vs C++ vs Java vs Javascript.",
                "Tech with Python (Software,Web,AI,ML).",
         ]
        for string in listing:
                object = Articals()
                object.title = string
                object.save()


        objects = Articals.objects.all()
        user = USER.objects.get( pk=1 ) 
        for object in objects:
                object.USER = user
                object.save()




def dummydatasubmission__():
        
        get = {
                'skills' : Skills(),
                'skillsof' : SkillsOf(),
                'skillsetsbuild' : SkillSetsBuild(),
                'skillsgroup' : SkillsGroup()
        }
        dictionary = {
                'skills' : [
                        'C', 'C++', 'Python', 'Java', 'Javascript', 'Go', 'Rust',
                        'HTML', 'CSS', 'jQuery', 'XML', 'Jinja', 
                        'Django', 'Django Rest Framework', 'JSON', 'React',
                        'SQLite', 'MySQL', 'MongoDB', 
                        'Git', 'GitHub', 'Docker',
                        
                        'Array', 'Linked List', 'Stack', 'Queue', 
                        'Hashing', 'Heap', 'Matrix',
                        'Tree', 'Binary Tree', 'Binary Search Tree', 
                        'Misc', 'Graph', 'DP', 'Trie',
                        'Advanced Data Structures'
                ],
                'skillsof' : [
                        'Programming Languages',
                        'Data Structures and Algorithms',
                        'System Designs', 
                        'Frameworks',
                        'Databases', 
                        'Others',
                ],
                'skillsgroups' : {
                        1 : [
                              'Frontend', 
                              'Backend', 
                              'DSA Based',
                        ],
                        2 : [
                              'Data Structures', 
                              'Algorithms', 
                        ],
                        3 : [
                              'Low Level Design', 
                              'High Level Design', 
                        ],
                        4 : [
                              'Frontend', 
                              'Backend', 
                              'Others',
                        ],
                        5 : [
                              'SQL', 
                              'NoSQL', 
                        ],
                },
        } 
        for key,values in dictionary.items(): 
                if key in ['skills','skillsof']: 
                        for value in values: 
                              object=get.get(key) 
                              object.name = value 
                              object.save() 
                else:
                        for id,values in values.items():
                              for value in values:
                                        skillsof = SkillsOf.objects.get(pk=id)
                                        object=get(key) 
                                        object.name = value 
                                        object.skillsof = skillsof
                                        object.save()
                              

        
        skillsof = SkillsOf.objects.get(pk=1)
        dicting = {
                1 : {
                    1 : [8,9,5,10,11,12],
                    2 : [1,2,3,4,6,7],
                    3 : [1,2,3,4,5,6,7],
                },
                4 : {
                        
                }
          }
        for id,values in dicting.items(): 
          skillsof = SkillsOf.objects.get(pk=id)
          for id,values in values.items(): 
                    skillsgroup = SkillsGroup.objects.get(pk=id)
                    for id in values: 
                              skills = Skills.objects.get(pk=id)
                              object = SkillSetsBuild()
                              object.skillsof = skillsof
                              object.skillsgroup = skillsgroup
                              object.skills = skills
                              object.save()


