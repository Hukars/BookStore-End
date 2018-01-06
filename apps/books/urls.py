from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^search/$', views.BookSearch.as_view()),
    url(r'^(?P<id>[0-9]+)/detail/$',views.BookDetail.as_view()),
    url(r'^list/$',views.BookList.as_view()),
    url(r'^creation/$', views.BookCreation.as_view()),
    url(r'^(?P<id>[0-9]+)/update/$', views.BookUpdate.as_view()),
    url(r'^(?P<id>[0-9]+)/delete/$', views.BookDelete.as_view()),
]