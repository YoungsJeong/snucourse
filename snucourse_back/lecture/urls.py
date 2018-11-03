from django.conf.urls import url
from .views import lecture_detail,write_opinion,lectureopinion_detail

urlpatterns = [
    url(r'^(?P<pk>\d+)/$',lecture_detail),
    url(r'^write_opinion/$', write_opinion),
    url(r'^opinion/?(?P<pk>\d+)/$', lectureopinion_detail),
]
