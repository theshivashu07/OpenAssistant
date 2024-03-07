from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),

		path('write/',views.write,name='write'),
		path('write/setup/',views.writesetup,name='writesetup'),
		# path('write/<int:id>/',views.write,name='write'),
		path('<str:from_>/',views.articals_from_,name='articals_from_'),
		path('open/<str:slug>/',views.open,name='open'),
                    
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),

]







