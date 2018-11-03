from lecture.models import Lecture
from user.models import GraduateCriteria
'''
major_mandatories = models.ManyToManyField(Lecture,related_name='major_mandatory') #전공선택
	major_optional = models.ManyToManyField(Lecture,related_name='major_optional') #전공필수
	science = models.ManyToManyField(Lecture,blank=True,related_name='science') #과학 과목명
	science_credit = models.IntegerField(null=False,blank=True,default=12) #과학 필수 이수학점
	language = models.ManyToManyField(Lecture,related_name='grad_language') #외국어 과목명
	language_credit = models.IntegerField(null=False,default=4) #외국어 필수 이수학점
	math = models.ManyToManyField(Lecture,blank=True,related_name='math') #수학 과목명
	math_credit = models.IntegerField(null=False,blank=True,default=6) #수학 필수 이수학점
	man_general_area = models.CharField(max_length=7,null=False,default='') #필수 교양 영역
	0 : 문화와예술
	1 : 생명과환경
	.
	.
	6 : 정치와경제
	for example) 015 means 0,1,5th is mandatory
	man_general_area_num = models.IntegerField(null=False,default=3) #필수 교양 영역 수
	#area_num is number of mandatory general studies area.
	#if max_general_area is 016 and man_general_area_num is 2, 
	#then one should take two courses out of [문화의예술,생명과환경,정치와경제]
	man_general_credit = models.IntegerField(null=False,default=6) #필수 교양 이수학점
	major_credit = models.IntegerField(null=False,default=62) #전공 최소 학점
	general_credit = models.IntegerField(null=False,default=44) #교양 최소 학점
	total_credit = models.IntegerField(null=False,default=130) #최소 학점
'''
def find(attr,key):
	str = 'a = Lecture.objects.filter('+attr+'=\'' + key +'\').values_list(\''+attr+'\', flat=True).distinct()'
	return str
Criteria = GraduateCriteria(science_credit=21,language_credit=4,math_credit=16,man_general_area='02346',man_general_area_num=2,man_general_credit=6,
major_credit=63,general_credit=44,total_credit=130)
Criteria.save()
major_mandatories = []
find('name','논리설계')
major_mandatories.append(a)




