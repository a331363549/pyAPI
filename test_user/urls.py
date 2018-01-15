from django.conf.urls import url
from test_user import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^userinfo/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^register/$',views.create_user),
    url(r'^login/$',views.login),
    url(r'^update/$',views.update_info),
]
