from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^teammembers/', views.getAllMembers),
    url(r'^member/(?P<member_id>[0-9A-Z]+)/$', views.redactTeamMember),
    url(r'^member/', views.addTeamMember),
]