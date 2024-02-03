from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
                    
		path('user/',views.user,name='user'),
		path('signup/',views.signup,name='signup'),
		path('login/',views.login,name='login'),
		# path('notifications/',views.notifications,name='notifications'),

]






