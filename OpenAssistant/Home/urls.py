from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
                    
		# path('notifications/',views.notifications,name='notifications'),

]



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)





