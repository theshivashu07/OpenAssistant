



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
        'Aarti' : {
                "Maa Durga'ji Aarti",
                "Satyanarayan'ji Aarti",
                "Shri Ram'ji Aarti",
                "Shri Ram Raksha Strot",
                "Hanuman Chalisha",
        },
        'Katha' : {
                "Satyanarayan'ji Katha", 
                "Ekadashi Katha", 
                "Guruwar Katha", 
        },
        'Mantra' : {
                "Surya Mantra", 
                "Shani Mantra", 
                "Maa Durga Mantra", 
                "Shaptsati Mantra", 
                "Chandra Mantra", 
        },
}




Database = {
        'Aarti' : {
                "Maa Durga'ji Aarti" : None,
                "Satyanarayan'ji Aarti" : None,
                "Shri Ram'ji Aarti" : None,
                "Shri Ram Raksha Strot" : None,
                "Hanuman Chalisha" : None,
        },
        'Katha' : {
                "Satyanarayan'ji Katha" : None, 
                "Ekadashi Katha" : None, 
                "Guruwar Katha" : None, 
        },
        'Mantra' : {
                "Surya Mantra" : None, 
                "Shani Mantra" : None, 
                "Maa Durga Mantra" : None, 
                "Shaptsati Mantra" : None, 
                "Chandra Mantra" : None, 
        },
}



SidebarTopicsLeft = {
        'basics' : [
                "Images",
                "Audios",
                "Reels",
                "Videos",
          ],
          'notes' : [
                "Mantra",
                "Aarti",
                "Kthaa"
          ],
          'others' : [
                  "Ekadashi Dates",
                  "Festival Dates",
                  "Other Saved Dates"
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
                        path = '/aadhyatm/'+keys.lower().replace(' ','-')+'/'
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
                        path = '/aadhyatm/'+value.lower().replace(' ','-')+'/'
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
                path = '/aadhyatm/'+value.lower().replace(' ','-')+'/'
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

















