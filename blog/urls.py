from django.urls import path

from . import views
from .views import Volunteers
from .views import PostCreateView,PostListView,EventCreateView,EventDetailView,InstantMessgeCreateView,ReportListView
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login,name='login'),
    path('success/',views.success_stories,name='success'),
    path('stories_of_need/',views.needy_stories,name='stories_of_need'),
    path('inspirational_stories/',views.inspirational_stories,name='inspirational_stories'),
    path('somevids/',views.some_videos,name='somevids'),
    path('volunteer/new/',views.volunteer_register,name='volunteer_join'),
    path('volunteers/',Volunteers.as_view(),name='volunteers'),
    path('events/',views.events,name='events'),
    path('join-trip/new/',views.join_trip,name='jointrip'),
    path('partner/new/',views.become_partner,name='become_a_partner'),
    path('partners/',views.partners,name='partners'),
    path('donate/',views.donate,name='donate'),
    path('reports/',ReportListView.as_view(),name='reports'),
    path('report/<int:id>/',views.report_detail,name='report_detail'),
    path('report/new/',views.create_report,name='create_report'),
    path('employees/',views.employees,name='employees'),
    path('messages/',views.user_messages,name='messages'),
    path('notification/new/',PostCreateView.as_view(),name='post_new'),
    path('posts/',PostListView.as_view(),name='posts'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('message/new/',InstantMessgeCreateView.as_view(),name='message_new'),
    path('main/',views.main,name='main'),
    path('messages/<int:id>/',views.instantmessage_detail,name='inmessage_detail'),
    path('newsletter/',views.news_letter,name='newsletter_create'),
    path('event/new/',EventCreateView.as_view(),name='event_new'),
    path('event/<int:pk>/',EventDetailView.as_view(),name="event_detail"),
    path('search/',views.search_post,name='search')
]