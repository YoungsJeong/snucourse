from django.contrib import admin
from .models import Lecture, LectureOpinion, LectureName

admin.site.register(Lecture)
admin.site.register(LectureOpinion)
admin.site.register(LectureName)
