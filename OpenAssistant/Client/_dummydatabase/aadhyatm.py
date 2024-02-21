








class Menus:
        def __init__(self,dictionary):
                self.name = dictionary.get('name',None)
                self.path = dictionary.get('path',None)
                self.logo = dictionary.get('logo',None)
                # print( self.name, self.path, self.logo )
        def __str__(self):
                return f"<object:Menus | name:{self.name}, url:{self.path}, logo:{self.logo}.>"


class Dicto:
        def __init__(self,dictionary):
                self.name = dictionary.get('name',None)
                self.value = dictionary.get('value',None)
                self.path = dictionary.get('path',None)
                self.logo = dictionary.get('logo',None)
                # print( self.name, self.path, self.logo )
        def __str__(self):
                return f"<object:Menus | name:{self.name}, url:{self.value}, name:{self.path},logo:{self.logo}.>"







Datasets = {
          'ProgrammingLanguages' : [
                    'C',
                    'C++',
                    'Python',
                    'Java',
                    'Javascript',
          ],
          'DataStructures' : [
                    'Array',
                    'String',
                    'Linked List',
                    'Stack',
                    'Queue',
                    'Matrix',
                    'Heap',
                    'Hashing',
                    'Graph',
                    'Tree',
                    'Binary Search Tree',
                    'Dynamic Programming',
          ],
}




Database = {
        'Problems' : {
                'Arrays' : 279,
                'Linked List' : 194,
                'Stack' : 173,
                'Queue' : 164,
                'Dequeue' : 153,
                'Heap' : 145,
        },
        'Solutions' : {
                'Python' : 329,
                'C++' : 192,
                'Java' : 126,
                'Javascript' : 27,
                'Go' : 23,
                'C' : 12,
        },
}



SidebarTopicsLeft = {
        'basics' : [
                    'Recent Problems',
                    'Most Viewed Problems',
                    'Most Liked Problems',
                    'Most Comment Problems',
          ],
          'notes' : [
                    'DSA Problems',
                    'SQL Problems',
                    'Pattern Problems',
                    'Design Problems',
                    'OOPs Problems',
          ],
          'others' : [
                    'Basic Problems', 
                    'Easy Problems', 
                    'Mediem Problems', 
                    'Hard Problems', 
          ],
        # 'Notes Problems', 
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



def getSidebarData_DICTS(database):
        '''actually this is fixed for youtube, but if want for another url, give app name only, like : 'problem' / 'artical' ..... '''
        Database = dict()
        for keys,values in database.items():
                objects = list()
                for key,value in values.items():
                        name, value, logo = key, value, None
                        path = '/problems/'+keys.lower().replace(' ','-')+'/'
                        dictionary = { 'name':name, 'value':value, 'path':path, 'logo':logo }
                        temp = Dicto(
                                dictionary = dictionary 
                        )
                        objects.append(temp)
                Database[keys] = objects
        return Database





def getSidebarData_DICT(database):
        '''actually this is fixed for youtube, but if want for another url, give app name only, like : 'problem' / 'artical' ..... '''
        Database = dict()
        for keys,values in database.items():
                objects = list()
                for value in values:
                        name, logo = value, None
                        path = '/problems/'+value.lower().replace(' ','-')+'/'
                        dictionary = { 'name':name, 'path':path, 'logo':logo }
                        temp = Menus(
                                dictionary = dictionary 
                        )
                        objects.append(temp)
                Database[keys] = objects
        return Database



def getSidebarData(database):
        '''actually this is fixed for youtube, but if want for another url, give app name only, like : 'problem' / 'artical' ..... '''
        Database = list()
        for value in database:
                name, logo = value, None
                path = '/problems/'+value.lower().replace(' ','-')+'/'
                dictionary = { 'name':name, 'path':path, 'logo':logo }
                object = Menus(
                        dictionary = dictionary
                )
                # print(object)
                Database.append(object)
        return Database













def AadhyatmRUN(dictionary=dict()):
        dictionary['DataSets'] = getSidebarData_DICT(Datasets)
        dictionary['sidebarleft'] = getSidebarData_DICT(SidebarTopicsLeft)
        dictionary['Database'] = getSidebarData_DICTS(Database)
        dictionary['sidebarright'] = getSidebarData(SidebarTopicsRight)
        return None





