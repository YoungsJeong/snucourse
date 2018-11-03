from django.db import models
from django.utils import timezone


class LectureName(models.Model):
    name = models.CharField(max_length=100, unique=True)
    credit = models.IntegerField(null=False, default=3)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    type = models.CharField(max_length=20, null=False)  # 교과구분
    college = models.ForeignKey('user.College', on_delete=models.CASCADE, null=True)  # 개설대학
    department = models.ForeignKey('user.Department', blank=True, on_delete=models.CASCADE, null=True)  # 개설학과
    degree = models.CharField(max_length=20, null=False)  # 이수과정
    grade = models.CharField(max_length=10, blank=True, null=False)  # 학년
    lecture_num = models.CharField(max_length=20, null=False)  # 교과목번호
    class_num = models.IntegerField(default=1, null=False)  # 강좌번호
    name = models.ForeignKey(LectureName, on_delete=models.CASCADE,  related_name="lecture")  # 교과목명
    credit_Total = models.IntegerField(null=False)	 # 총학점
    credit_Theory = models.IntegerField(blank=True, null=False)	 # 강의학점
    credit_Practice = models.IntegerField(blank=True, null=False)	 # 실습학점
    time = models.CharField(max_length=20, blank=True, null=False)	 # 수업교시
    composition = models.CharField(max_length=20, blank=True, null=False)  # 수업형태
    classroom = models.CharField(max_length=20, blank=True, null=False)  # 강의실
    lecturer = models.CharField(max_length=20, blank=True, null=False)  # 담당교수
    capacity = models.CharField(max_length=20, null=False)   # 정원
    optional = models.CharField(max_length=100, blank=False, null=False)   # 비고
    language = models.CharField(max_length=20, null=False)   # 강의언어
    area = models.CharField(max_length=20, null=False, blank=True)   # 교양영역
    easy = models.IntegerField(null=False, blank = True, default=0)  # 널널함
    useful = models.IntegerField(null=False, blank = True, default=0)  # 유익함
    credit = models.IntegerField(null=False, blank = True, default=0)  # 학점만족
    avg_review_score = models.FloatField(null=False, blank=True, default=0)

    def __str__(self):
        return self.name.name


class LectureOpinion(models.Model):
    content = models.TextField(max_length=500, null=False)
    created_date = models.DateTimeField(default=timezone.now, null=False)
    lecture	= models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True)
    easy = models.IntegerField(null=False)  # 널널함
    useful = models.IntegerField(null=False)  # 유익함
    credit = models.IntegerField(null=False)  # 학점만족

    def __str__(self):
        if self.lecture is not None:
            return "%s - %s" % (self.lecture.name,  '의 강의평')
        return "강의평"
