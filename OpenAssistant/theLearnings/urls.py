from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		path('<str:skillsof_>/',views.learnings_from_,name='learnings_from_'),
		path('<str:skillsof_>/<str:skills_>/',views.learnings_from_,name='learnings_from_'),

		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),

]













