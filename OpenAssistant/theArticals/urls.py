from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
		# path('<slug:skillsetsbuild>/',views.write,name='write'),
		# path('<slug:skillsetsbuild>/<slug:skillspointers>/',views.write,name='write'),
                    
		path('options/<slug:optionname>/',views.ShowMyArtical,name='ShowByOption'),
                    
		path('<str:skillsetsbuild>/',views.ShowRelatedArticals,name='ShowRelatedArticals'),
		path('<str:skillsetsbuild>/<str:skillspointers>/',views.ShowMyArtical,name='ShowMyArtical'),
                    
		path('write/',views.write,name='write'),
		path('show/',views.show,name='show'),
		# path('write/setup/',views.writesetup,name='writesetup'),
		# path('write/<int:id>/',views.write,name='write'),
		path('<str:from_>/',views.articals_from_,name='articals_from_'),
		path('open/<str:slug>/',views.open,name='open'),
                    
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),

]







