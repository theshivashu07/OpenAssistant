from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),

		# aur-all-apps-dummy-collections : we activate this till the app not haven...
		# path('profile/',views.profile_metaverse,name='profile_metaverse'),
		path('login/',views.login,name='login'),
		path('logout/',views.logout,name='logout'),
		path('signup/',views.signup,name='signup'),
		path('profile-setup/',views.profilesetup,name='profile-setup'),
		path('reset-password/',views.resetpassword,name='resetpassword'),
		path('asked-questions/',views.askedquestions,name='askedquestions'),
		path('users-list/',views.userslist,name='userslist'),
		path('default-user/',views.defaultuser,name='defaultuser'),
                    
		
		# path('emailvalidation/',views.emailvalidation,name='emailvalidation'),
		# path('index/',views.index,name='index'),

]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)





