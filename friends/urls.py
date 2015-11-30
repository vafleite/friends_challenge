from django.conf.urls import url
from friends import views

urlpatterns = [
    url(r'^me$', views.Me.as_view()),
    url(r'^reset$', views.Reset.as_view()),
    url(r'^nearest$', views.Nearest.as_view()),
    url(r'^nearest/(?P<near_num>\d+)$', views.Nearest.as_view()),
]

