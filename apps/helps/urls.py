from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^rules/add/$',views.AddRule.as_view()),
    url(r'^rules/(?P<id>[0-9]+)/delete/$',views.DeleteRule.as_view()),
    url(r'^rules/(?P<id>[0-9]+)/update/$',views.UpdateRule.as_view()),
    url(r'^rules/$',views.SystemRuleList.as_view()),
    url(r'^problems/$',views.CommonProblemList.as_view()),
]