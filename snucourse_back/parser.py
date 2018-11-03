from lecture.models import Lecture,LectureName
from user.models import Department,College
from lecture.serializers import LectureSerializer
file = open('courses.txt','r',encoding='UTF-8')
datas = file.readlines()
for data in datas:
	data = data.split('\t')
	colle = College.objects.filter(name=data[1])
	if(colle.count()==0):
		colle = College(name=data[1])
		colle.save()
	else: colle = colle[0]
	depart = Department.objects.filter(name=data[2])
	if(depart.count()==0):
		depart = Department(name=data[2],college=colle)
		depart.save()
	else: depart = depart[0]
	lecturename = LectureName.objects.filter(name=data[7])
	if(lecturename.count()==0):
		lecturename = LectureName(name=data[7])
		lecturename.save()
	else: lecturename = lecturename[0]
	lecture = Lecture(type = data[0],college=colle,department = depart,degree = data[3],grade=data[4], lecture_num=data[5], class_num = data[6],
	name= lecturename, credit_Total = data[8], credit_Theory= data[9],credit_Practice=data[10],time=data[11],composition =data[12],classroom=data[13],
	lecturer=data[14],capacity=data[15],optional=data[16],language=data[17])
	lecture.save()