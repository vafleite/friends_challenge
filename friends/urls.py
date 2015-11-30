from django.conf.urls import url
from friends import views

urlpatterns = [
    url(r'^me$', views.Me.as_view()),
    url(r'^reset$', views.Reset.as_view()),
    url(r'^me/nearest$', views.Nearest.as_view()),
    url(r'^me/nearest/(?P<near_num>\d+)$', views.Nearest.as_view()),
    url(r'^friends$', views.Friends.as_view()),
    url(r'^friends/(?P<pk>\d+)$', views.FriendsDetails.as_view()),
    url(
        r'^route/from/(?P<from_id>\d+)/to/(?P<to_id>\d+)$',
        views.RouteTo.as_view()
    ),
    url(
        r'^route/to/(?P<to_id>\d+)$',
        views.RouteTo.as_view()
    ),
    url(
        r'^route/from/me/to/(?P<to_id>\d+)$',
        views.RouteTo.as_view()
    ),
]

