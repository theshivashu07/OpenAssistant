from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
                    
		
		path('showlogo/',views.showlogo,name='showlogo'), 
                    
		
		path('<str:skillsof_>/',views.learnings_from_,name='learnings_from_'),
		# path('<str:skillsof_>/<str:skills_>/',views.learnings_from_,name='learnings_from_'),

		path('options/<str:skillof>/',views.options,name='options'), 
		path('<str:skillof>/<str:skill>/',views.skills,name='skills'), 
		path('<str:skillof>/<str:skill>/<str:heading>/<str:subheading>/<str:topic>/',views.showtopic,name='showtopic'), 
		
		# http://localhost:1234/admin/theLearnings/topic/74/change/	

                    # path(r'^(.*)$', views.index), 

		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),


]













