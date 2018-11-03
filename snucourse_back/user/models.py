from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from lecture.models import Lecture, LectureOpinion, LectureName
from .manager import UserManager
from django.utils.translation import ugettext_lazy as _


class College(models.Model):
    name = models.CharField(blank=False, null=False, max_length=128)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(blank=False, null=False, max_length=128)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GraduateCriteria(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=1)
    year = models.IntegerField(null=False,blank=False,default=2015)
    major_mandatories = models.ManyToManyField(LectureName,related_name='major_mandatory') #전공선택
    major_optional = models.ManyToManyField(LectureName,related_name='major_optional') #전공필수
    sociality = models.ManyToManyField(LectureName,related_name='sociality',blank=True)
    creativity = models.ManyToManyField(LectureName,related_name='creativity',blank=True)
    science = models.ManyToManyField(LectureName,blank=True,related_name='science') #과학 과목명. 컴개실 포함
    science_credit = models.IntegerField(null=False,blank=True,default=12) #과학 필수 이수학점
    language = models.ManyToManyField(LectureName,related_name='grad_language') #외국어 과목명
    language_credit = models.IntegerField(null=False,default=4)#외국어 필수 이수학점
    math = models.ManyToManyField(LectureName,blank=True,related_name='math') #수학 과목명 컴개실 포함
    math_credit = models.IntegerField(null=False,blank=True,default=6) #수학 필수 이수학점
    man_general_area = models.CharField(max_length=40,null=False,default='') #필수 교양 영역
    #문화와예술
    #생명과환경
    #.
    #.
    #정치와경제
    #for example) 문화와예술|생명과환경|정치와경제
    man_general_area_num = models.IntegerField(null=False,default=3) #필수 교양 영역 수
    #area_num is number of mandatory general studies area.
    #if max_general_area is 문화와예술|생명과환경|정치와경제 and man_general_area_num is 2,
    #then one should take two courses in [문화의예술,생명과환경,정치와경제]
    major_credit = models.IntegerField(null=False,default=62) #전공 최소 학점
    general_credit = models.IntegerField(null=False,default=44) #교양 최소 학점
    total_credit = models.IntegerField(null=False,default=130) #최소 학점


class User(AbstractBaseUser, PermissionsMixin):
    # Primitive Fields
    name = models.CharField(blank=False, null=False, max_length=128)
    student_id = models.IntegerField(unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    # Relative Fields
    major = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="user_minor", null=True)  # 주전공
    minor = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="user_major", null=True)  # 부전공
    double_major = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="user_double_major", null=True)  # 복수전공
    lectures = models.ManyToManyField(LectureName, blank=True)
    lecture_opinions = models.ManyToManyField(LectureOpinion, blank=True)
    graduate_criteria = models.ManyToManyField(GraduateCriteria, blank=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

