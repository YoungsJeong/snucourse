from lecture.models import Lecture,LectureName
from user.models import Department,College
from lecture.serializers import LectureSerializer
import glob


def update(filename):
    file = open(filename,encoding='UTF-8')
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
            lecturename = LectureName(name=data[7],credit=data[9])
            lecturename.save()
        else: lecturename = lecturename[0]
        lecture = Lecture.objects.filter(name=lecturename,lecturer = data[15])
        if(lecture.count==0):
            lecture = Lecture(type = data[0],college=colle,department = depart,degree = data[3],grade=data[4], lecture_num=data[5], class_num = data[6],
            name= lecturename, credit_Total = data[9], credit_Theory= data[10],credit_Practice=data[11],time=data[12],composition =data[13],classroom=data[14],
            lecturer=data[15],capacity=data[16],optional=data[18],language=data[19])
            lecture.save()


files = glob.glob('all\*.txt')
for file in files:
    update(file)
