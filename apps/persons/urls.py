from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^adminLogin/$',views.AdminLogin.as_view()),
    url(r'^userRegister/$',views.UserRegister.as_view()),
    url(r'^userLogin/$',views.UserLogin.as_view()),
    url(r'^userLogout/$', views.UserLogout.as_view())
]