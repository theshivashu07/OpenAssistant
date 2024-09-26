


from theArticals.models import *
# from theArticals.management import classes
# from API.Code.Management import sessions
# from API.Code.Management.Sessions import UserExists
from theArticals.management import classes as  CLASSES
from API.Code.Management import Sessions as SESSIONS


def get_recent_articals(*args,**kwargs):
          ''' ( start=5, last=5 ) '''
          articals = Articals.objects.all()
          


def CollectingData( request,dictionary=dict() ):
        
        user = SESSIONS.UserExists(request)
        CLASSES.format_user_for_header( UserExists )












