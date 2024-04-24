from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		path('<str:skillsof_>/',views.learnings_from_,name='learnings_from_'),
		# path('<str:skillsof_>/<str:skills_>/',views.learnings_from_,name='learnings_from_'),

		path('options/<str:skillof>/',views.options,name='options'), 
		path('<str:skillof>/<str:skill>/',views.skills,name='skills'), 
		path('<str:skillof>/<str:skill>/<str:heading>/<str:subheading>/<str:topic>/',views.showtopic,name='showtopic'), 

                    # path(r'^(.*)$', views.index), 

		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),

]













