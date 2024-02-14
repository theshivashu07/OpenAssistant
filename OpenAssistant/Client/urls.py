from django.urls import path
from . import views


urlpatterns=[
		path('',views.index,name='index'),
		# path('index/',views.index,name='index'),
                    
		path('notifications/',views.notifications,name='notifications'),
                    
		path('profile/',views.profile,name='profile'),
		path('profile/edit/',views.profile_edit,name='profile_edit'),
                    
		path('articals/',views.articals,name='articals'),
		path('articals/<slug:artical_slug>/',views.artical_open,name='artical_open'),
		path('articals/edit/<slug:artical_slug>/',views.artical_edit,name='artical_edit'),
		path('articals/report/<slug:artical_slug>/',views.artical_report,name='artical_report'),
		path('articals/suggestion/<slug:artical_slug>/',views.artical_suggestion,name='artical_suggestion'),
		path('articals/ask/<slug:artical_slug>/',views.artical_ask,name='artical_ask'),
                    
		path('problems/',views.problems,name='problems'),
		path('problems/<slug:problem_slug>/',views.problem_open,name='problem_open'),
		path('problems/edit/<slug:problem_slug>/',views.problem_edit,name='problem_edit'),
		path('problems/report/<slug:problem_slug>/',views.problem_report,name='problem_report'),
		path('problems/suggestion/<slug:problem_slug>/',views.problem_suggestion,name='problem_suggestion'),
		path('problems/ask/<slug:problem_slug>/',views.problem_ask,name='problem_ask'),
                    
		path('youtube/',views.youtube,name='youtube'),
		path('youtube/<slug:youtube_link>/',views.youtube_open,name='youtube_open'),
		path('youtube/edit/<slug:youtube_link>/',views.youtube_edit,name='youtube_edit'),
		path('youtube/report/<slug:youtube_link>/',views.youtube_report,name='youtube_report'),
		path('youtube/suggestion/<slug:youtube_link>/',views.youtube_suggestion,name='youtube_suggestion'),
		path('youtube/ask/<slug:youtube_link>/',views.youtube_ask,name='youtube_ask'),





		path('report/?type=problem/artical/youtube,slug=xwasyeweygdiuhjsj13546',views.report,name='report'),
		path('suggestion/?type=problem/artical/youtube,slug=xwasyeweygdiuhjsj13546',views.suggestion,name='suggestion'),
		path('ask/?type=problem/artical/youtube,slug=xwasyeweygdiuhjsj13546',views.ask,name='ask'),

		path('report/?type=problem&slug=xwasyewsj13546',views.report,name='report'),
		path('suggestion/?type=youtube&slug=xwasyewsj13546',views.suggestion,name='suggestion'),
		path('ask/?type=artical&slug=xwasyewsj13546',views.ask,name='ask'),








		path('hireus/',views.hireus,name='hireus'),
                    
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),
		# path('youtube/',views.youtube,name='youtube'),

]






