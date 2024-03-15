

from Home.models import USER
from theArticals.models import Articals
import datetime


def getDay(datetime):
        database = {
                0 : 'Monday',
                1 : 'Tuesdat',
                2 : 'Wednesday',
                3 : 'Thursday',
                4 : 'Friday',
                5 : 'Saturday',
                6 : 'Sunday',
        }
        key = datetime.weekday()
        return database.get( key,None )

def getDate(datetime):
        return datetime.date() 


# def getAgo(datetime):
def getAgo(prev):
        curr = datetime.datetime.today()

        dictt = {
                'year' : curr.year-prev.year,
                'month' : curr.month-prev.month,
                'day' : curr.day-prev.day,
                'hour' : curr.hour-prev.hour,
                'minute' : curr.minute-prev.minute,
                'second' : curr.second-prev.second,
                'microsecond' : curr.microsecond-prev.microsecond,
        }
        # print(prev,curr)
        # print(dictt)
        
        def filter(data,string):
                if data!=1:
                        string+='s'
                return f"{data} {string} ago"
        
        string = ""
        if dictt['year']:
                return filter(dictt['year'],'year')
        elif dictt['month']:
                return filter(dictt['month'],'month')
        elif dictt['day']:
                return filter(dictt['day'],'day')
        elif dictt['hour']:
                return filter(dictt['hour'],'hour')
        elif dictt['minute']:
                return filter(dictt['minute'],'minute')
        elif dictt['second']:
                return filter(dictt['second'],'second')
        # else: # elif dictt['microsecond']:
        return filter(dictt['microsecond'],'microsecond')







class Articals:
        def __init__(self,objectArtical):
                
                self.user = {
                        'fullname' : objectArtical.USER.FullName,
                        'username' : objectArtical.USER.Username,
                        # 'url' : None, 
                }
                self.artical = {
                        'title' : objectArtical.title, 
                        'important' : objectArtical.important, 
                        'url' : None, 
                }
                self.details = {
                        'date' : getDate(  ), 
                        'day' : getDay(  ), 
                        'ago' : getAgo(  ), 
                        'views' : None,
                        'likes' : None,
                        'comments' : None,
                        'reports' : None,
                        'suggestions' : None,
                        'varify' : None,
                }





def recent_articals(request):

          articals = Articals.objects.all()

          for artical in articals:
                  pass
                  
                  















