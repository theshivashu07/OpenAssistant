from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
                    
		path('notifications/',views.notifications,name='notifications'),
                    
		path('profile/',views.profile,name='profile'),
		path('profile/edit/',views.profile_edit,name='profile_edit'),
                    
		path('articals/',views.articals,name='articals'),
		path('articals/<str:from_>/',views.articals_from_,name='articals_from_'),
                    
		path('problems/',views.problems,name='problems'),
		path('problems/<str:from_>/',views.problems_from_,name='problems_from_'),
                    
		path('youtube/',views.youtube,name='youtube'),
		path('youtube/<str:from_>/',views.youtube_from_,name='youtube_from_'),
                    
		path('aadhyatm/',views.aadhyatm,name='aadhyatm'),
		path('aadhyatm/<str:from_>/',views.aadhyatm_from_,name='aadhyatm_from_'),

		path('hireus/',views.hireus,name='hireus'),
                    







		



		# path('report/?type=problem/artical/youtube,slug=xwasyeweygdiuhjsj13546',views.report,name='report'),
		# path('suggestion/?type=problem/artical/youtube,slug=xwasyeweygdiuhjsj13546',views.suggestion,name='suggestion'),
		# path('ask/?type=problem/artical/youtube,slug=xwasyeweygdiuhjsj13546',views.ask,name='ask'),

		# path('report/?type=problem&slug=xwasyewsj13546',views.report,name='report'),
		# path('suggestion/?type=youtube&slug=xwasyewsj13546',views.suggestion,name='suggestion'),
		# path('ask/?type=artical&slug=xwasyewsj13546',views.ask,name='ask'),



		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),


]






