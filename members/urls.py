from django.conf.urls import url
from . import views

app_name = 'members'

urlpatterns = [

    url(r'^members/$', views.member_list),
    url(r'^members/(?P<pk>[0-9]+)/*$', views.member_detail),
    url(r'^members/create/*$', views.create_member),

]
