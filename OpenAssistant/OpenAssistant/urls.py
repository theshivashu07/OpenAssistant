"""OpenAssistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from theLearnings.views import fast404

# HANDLER404 = 'theLearnings.views.handler404' 
handler404 = 'theLearnings.views.handler404'  


from Home.views_google import google_login

urlpatterns = [
 
    path('admin/', admin.site.urls),

    # all auth - google, facebook, github
    path('accounts/', include('allauth.urls')), 
    path("google-login/", google_login, name="google_login"),

    # path('Admin/', include('Admin.urls')),
    path('developer/', include('Admin.urls')),

    # path('Client/', include('Client.urls')),
    path('', include('Client.urls')),

    # path('Home/', include('Home.urls')),
    path('security/', include('Home.urls')),

    # path('API/', include('API.urls')),
    path('api/', include('API.urls')),

    # Other Paths
    path('articals/', include('theArticals.urls')),
    path('problems/', include('theProblems.urls')),
    path('learnings/', include('theLearnings.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')), 

    # path('404/', TemplateView.as_view(template_name='theLearnings/Client/404.html'), name='404'), 

    # path('fast404/', include('theLearnings.views.fast404')),
    path('fast404/', fast404, name='fast404'),
    
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_ROOT)



