from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    url(r'^cartItems/$',views.ShoppingCartList.as_view()),
    url(r'^cartItems/(?P<id>[0-9]+)/delete/$',views.DeleteCart.as_view()),
    url(r'^cartItems/(?P<id>[0-9]+)/update/$',views.UpdateCart.as_view()),
    url(r'^cartItems/add/$',views.AddCart.as_view()),
    url(r'^orders/add/$',views.AddOrder.as_view()),
    url(r'^orders/(?P<id>[0-9]+)/delete/$',views.DeleteOrder.as_view()),
    url(r'^orders/$',views.OrderList.as_view()),
    url(r'^orders/(?P<id>[0-9]+)/records/$',views.RecordList.as_view()),
    url(r'^orders/(?P<id>[0-9]+)/update/$', views.UpdateOrder.as_view()),
    url(r'^allOrders/$',views.AllOrders.as_view()),
]