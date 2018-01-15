from django.conf.urls import url
from test_user import views

urlpatterns = [
    url(r'^snippets/$', views.user_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^register/$',views.create_user),
    url(r'^login/$',views.login)
]
