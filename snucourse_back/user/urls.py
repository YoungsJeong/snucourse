from django.conf.urls import url
from .views import signup, login, register_lectures, get_user_info, check_graduate

urlpatterns = [
    url(r'^signup/$', signup),
    url(r'^login/$', login),
    url(r'^register_lectures/$', register_lectures),
    url(r'^info/$', get_user_info),
    url(r'^graduate_assessment/$',check_graduate),
]
