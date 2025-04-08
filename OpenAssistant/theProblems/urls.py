from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
                    

		path('openproblem/',views.openproblem,name='openproblem'),

		path('<str:from_>/',views.problems_from_,name='problems_from_'),
                    
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),

]







