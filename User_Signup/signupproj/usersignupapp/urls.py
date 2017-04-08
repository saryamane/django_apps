from django.conf.urls import url
from usersignupapp import views

urlpatterns = [
    url(r'^$', views.users, name = 'users'),
]
