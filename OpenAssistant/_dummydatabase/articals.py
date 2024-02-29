





class Menus:
        def __init__(self,dictionary):
                self.name = dictionary.get('name',None)
                self.path = dictionary.get('path',None)
                self.logo = dictionary.get('logo',None)
                # print( self.name, self.path, self.logo )
        def __str__(self):
                return f"<object:Menus | name:{self.name}, url:{self.path}, logo:{self.logo}.>"


# Topics = {
#           'Mains' : {
#                     'Python' : { 'name' : 'Home', 'Python' : '/articals/python/', 'logo' : 'fa-brands fa-python'}, 
#           },
#           'Others' : {
                    
#           }
# }


ScrollbarTopics = [
          'C',
          'C++',
          'Python',
          'Java',
          'Javascript',
          'HTML',
          'CSS',
          # 'Django',
          'Django Rest Framework',
          'Data Structure and Algorithm',
          'System Designs',
          'GitHub',
          'MySQL',
          'MongoDB',
          'Interview Praprations',
          'Interview Experience', 
          'Rest API',
          'Jinja',
]

SidebarTopicsLeft = [
        'Recent Articals',
        'Most Viewed Articals',
        'Most Liked Articals',
        'Most Comment Articals',
        'Programming Articals',
        'Notes Articals',
        'Political Articals', 
        'Geo Political Articals', 
        # 'Notes Articals', 
]

SidebarTopicsLeft = {
        'basics' : [
                    'Recent Articals',
                    'Most Viewed Articals',
                    'Most Liked Articals',
                    'Most Comment Articals',
          ],
          'notes' : [
                    'DSA Articals',
                    # 'Algorithms Articals',
                    # 'Data Structure Articals',
                    'Database Articals',
                    'System Design Articals',
                    'Programming Articals',
                    'Other Articals',
          ],
          'others' : [
                    'Political Articals', 
                    'Geo Political Articals', 
          ],
        # 'Notes Articals', 
}

SidebarTopicsRight = [
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

Articals = {
        
}


def filter(name):
        string=''
        for ch in name:
                if ch==' ':
                        string+='-'
                        continue
                temp = ord(ch)
                if temp>=65 and temp<=90:
                        ch = chr(temp+32)
                        string+=ch
                elif temp>=97 and temp<=122:
                        string+=ch
                elif temp>=48 and temp<=57:
                        string+=ch
        return string


def getSidebarData_DICT(database,extraadd=''):
        '''actually this is fixed for youtube, but if want for another url, give app name only, like : 'problem' / 'artical' ..... '''
        Database = dict()
        for keys,values in database.items():
                objects = list()
                for value in values:
                        name, logo = value, None
                        # path = '/articals/'+extraadd+value.lower().replace(' ','-')+'/'
                        path = '/articals/'+extraadd+filter(value)+'/'
                        dictionary = { 'name':name, 'path':path, 'logo':logo }
                        temp = Menus(
                                dictionary = dictionary 
                        )
                        objects.append(temp)
                Database[keys] = objects
        return Database




def getSidebarData(database,extraadd=''):
        '''actually this is fixed for youtube, but if want for another url, give app name only, like : 'problem' / 'artical' ..... '''
        if extraadd!='':
                extraadd=extraadd+"/"
        Database = list()
        for value in database:
                name, logo = value, None
                # path = '/articals/'+extraadd+value.lower().replace(' ','-')+'/'
                path = '/articals/'+extraadd+filter(value)+'/'
                dictionary = { 'name':name, 'path':path, 'logo':logo }
                object = Menus(
                        dictionary = dictionary
                )
                # print(object)
                Database.append(object)
        return Database




def ArticalsRUN(dictionary=dict()):
        dictionary['scrollbar'] = getSidebarData(ScrollbarTopics)
        dictionary['sidebarleft'] = getSidebarData_DICT(SidebarTopicsLeft)
        dictionary['sidebarright'] = getSidebarData(SidebarTopicsRight,'open')
        return None











