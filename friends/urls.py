from django.conf.urls import url
from friends import views

urlpatterns = [
    url(r'^me$', views.Me.as_view()),
]

