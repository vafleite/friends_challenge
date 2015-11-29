from django.conf.urls import url
from friends import views

urlpatterns = [
    url(r'^start$', views.start),
]

