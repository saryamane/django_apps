from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.user_signup, name='signup'),
    url(r'^help/', views.help_page, name='help'),
]
