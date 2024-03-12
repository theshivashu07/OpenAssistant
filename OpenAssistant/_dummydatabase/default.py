


from theArticals.models import *
from Home.models import *
from API.models import *




def submitdummydata(user=None):
          dummydatasubmission()
          dummydatasubmission_()
          dummydatasubmission__()
          return



def dummydatasubmission():
        ''' Articals All Database Sets to RUN '''
        ''' Actions(), ContentFrom(), ContentOf(),  '''


        listing = [ 'SignUp', 'LogIn', 'Logout', 'Rejoin', 'Temporary Delete', 'Permanent Delete' ] 
        for string in listing: 
                object = Actions() 
                object.name = string 
                object.save() 

        '''
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
        '''
                
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
        
        user = USER()
        user.FullName = "SHivam SHukla"
        user.FirstName = "SHivam"
        user.LastName = "SHukla"
        user.Username = "theshivashu"
        user.Mobile = "7898565074"
        user.Email = "theshivashu@gmail.com"
        user.Password = "12345"
        user.isChecked = True 
        user.save()

        objects = Articals.objects.all()
        # user = USER.objects.get( pk=1 ) 
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
                        # 01-07
                        'C', 'C++', 'Python', 'Java', 'Javascript', 'Go', 'Rust',
                        # 08-12
                        'HTML', 'CSS', 'jQuery', 'XML', 'Jinja', 
                        # 13-16
                        'Django', 'Django Rest Framework', 'React', 'Bootstrap',
                        # 17-19
                        'SQLite', 'MySQL', 'MongoDB', 
                        # 20-22
                        'Git', 'GitHub', 'Docker',
                        
                        #23-36
                        'Array', 'Linked List', 'Stack', 'Queue',  
                        'Hashing', 'Heap', 'Matrix', 
                        'Tree', 'Binary Tree', 'Binary Search Tree', 
                        'Misc', 'Graph', 'DP', 'Trie',
                        #37-38
                        'Advanced Data Structures', 'Others'
                ],
                
                'skillsof' : [
                        'Programming Languages',
                        'Data Structures and Algorithms',
                        'System Designs', 
                        'Frameworks',
                        'Databases', 
                        'Others',
                ],
                
                'skillsgroup' : {
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
                              'Bothend'
                        ],
                        5 : [
                              'SQL', 
                              'NoSQL', 
                        ],
                },
                
                'skillsetsbuild' : {
                        1 : {
                                1 : [8,9,5,10,11,12], 
                                2 : [1,2,3,4,6,7], 
                                3 : [1,2,3,4,5,6,7], 
                        },
                        2 : {
                                4 : [ 23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38 ], 
                                5 : [  ], 
                        },
                        4 : {
                                8 : [ 15,16 ], 
                                9 : [ 13,14 ], 
                                10 : [  ], 
                        },
                        5 : {
                                11 : [ 17,18 ], 
                                12 : [ 19 ], 
                        },
                },
        } 
        
        # for key,values in dictionary.items(): 
        values = dictionary.get('skills')
        for value in values: 
                object=Skills()
                object.name = value 
                object.save() 

        values = dictionary.get('skillsof')
        for value in values: 
                object=SkillsOf()
                object.name = value 
                object.save() 

        values = dictionary.get('skillsgroup')
        for id,values in values.items():
                skillsof = SkillsOf.objects.get(pk=id)
                for value in values:
                        object=SkillsGroup()
                        object.name = value 
                        object.skillsof = skillsof
                        object.save()

        values = dictionary.get('skillsetsbuild')
        for id,values in values.items(): 
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


        print(f"API's Apps all data insertion done !!!") 
                              


