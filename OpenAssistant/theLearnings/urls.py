from django.urls import path
from . import views





from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, SkillOfViewSet, HeadingViewSet, SubheadingViewSet, TopicViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'skillof', SkillOfViewSet)
router.register(r'headings', HeadingViewSet)
router.register(r'subheadings', SubheadingViewSet)
router.register(r'topics', TopicViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]







urlpatterns += [
		path('',views.index,name='index'),
                    
		
		path('resting/',views.resting,name='resting'),


		path('showlogo/',views.showlogo,name='showlogo'), 
                    
		
		path('<str:skillsof_>/',views.learnings_from_,name='learnings_from_'),
		# path('<str:skillsof_>/<str:skills_>/',views.learnings_from_,name='learnings_from_'),

		path('options/<str:skillof>/',views.options,name='options'), 
		path('<str:skillof>/<str:skill>/',views.skills,name='skills'), 
		path('<str:skillof>/<str:skill>/<str:heading>/<str:subheading>/<str:topic>/',views.showtopic,name='showtopic'), 
		

		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),
		# path('open/',views.open,name='open'),


]










