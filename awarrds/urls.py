from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns= [
    path('', views.index, name='index'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^projects/$', views.project, name='project'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
]