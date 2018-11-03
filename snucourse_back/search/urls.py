from django.conf.urls import url
from .views import search_lecture_name, search_department, search_lecture_detail


urlpatterns = [
    url(r'^lecture_name/?$', search_lecture_name),
    url(r'^department/?$', search_department),
    url(r'^lecture_detail/?$', search_lecture_detail),
]
