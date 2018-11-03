from user.models import User,GraduateCriteria
from lecture.models import Lecture,LectureName
import json


class grad_message:
    def __init__(self,major_need,sociality_need,creativity_need,science_need,
                 language_need,math_need,area_need,major_credit_need,general_credit_need,
                 total_credit_need, took_major_credit, took_general_credit,took_total_credit):
        self.major_need = major_need
        self.sociality_need = sociality_need
        self.creativity_need = creativity_need
        self.science_need = science_need
        self.language_need = language_need
        self.math_need = math_need
        self.area_need = area_need
        self.major_credit_need = major_credit_need
        self.general_credit_need = general_credit_need
        self.total_credit_need = total_credit_need
        self.took_major_credit = took_major_credit
        self.took_general_credit = took_general_credit
        self.took_total_credit = took_total_credit
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)

def general_area(area,lectures):
    area = '학문의세계_'+area
    criteria = Lecture.objects.filter(area=area)
    for lecture in criteria:
        if lecture.name in lectures:
            lectures.remove(lecture.name)
            return True
    return False

def toMessage(lectures,criteria):
    major_need = []
    major_credit = 0
    sociality = False
    creativity = False
    general_credit = 0
    lectures = list(lectures.all())
    for lecture in criteria.major_mandatories.all():
        if '|' in lecture.name:
            check = False
            names = lecture.name.split('|')
            for name in names:
                for lec in lectures:
                    if(name==lec.name):
                        major_credit = major_credit+lecture.credit
                        lectures.remove(lec)
                        check = True
                        break
                if(check): break
            if(check==False):major_need.append(lecture.name)
        else:
            if not lecture in lectures:
                major_need.append(lecture.name)
            else:
                major_credit = major_credit+lecture.credit
                lectures.remove(lecture)

    for lecture in criteria.major_optional.all():
        if lecture in lectures:
            major_credit = major_credit+lecture.credit
            temp = list(criteria.sociality.all())
            if lecture in temp:
                sociality = True
                lectures.remove(lecture)
            temp = list(criteria.creativity.all())
            if lecture in temp:
                creativity = True
                lectures.remove(lecture)

    for lecture in criteria.sociality.all():
        if lecture in lectures:
            general_credit = general_credit+lecture.credit
            sociality = True
            lectures.remove(lecture)
    for lecture in criteria.creativity.all():
        if lecture in lectures:
            general_credit = general_credit+lecture.credit
            creativity = True
            lectures.remove(lecture)
    science_credit =0
    for lecture in criteria.science.all():
        if '|' in lecture.name:
            check = False
            names = lecture.name.split('|')
            for name in names:
                for lec in lectures:
                    if(name==lec.name):
                        general_credit = general_credit+lecture.credit
                        science_credit = science_credit+lecture.credit
                        lectures.remove(lec)
                        check = True
                        break
                if(check): break
        else:
            if lecture in lectures:
                general_credit = general_credit+lecture.credit
                science_credit = science_credit+lecture.credit
                lectures.remove(lecture)
    language_credit = 0
    for lecture in criteria.language.all():
        if lecture in lectures:
            general_credit = general_credit+lecture.credit
            language_credit = language_credit+lecture.credit
            lectures.remove(lecture)
    math_credit =0
    math_need = []
    for lecture in criteria.math.all():
        if '|' in lecture.name:
            check = False
            names = lecture.name.split('|')
            for name in names:
                for lec in lectures:
                    if(name==lec.name):
                        general_credit = general_credit+lecture.credit
                        math_credit = math_credit+lecture.credit
                        lectures.remove(lec)
                        check = True
                        break
                if(check): break
            if(check==False):math_need.append(lecture.name)
        else:
            if lecture in lectures:
                general_credit = general_credit+lecture.credit
                math_credit = math_credit+lecture.credit
                lectures.remove(lecture)
            else:
                math_need.append(lecture.name)
    took_area =[]
    need_number=0
    area_need = []
    for area in criteria.man_general_area.split('|'):
        if(general_area(area,lectures)):
            general_credit = general_credit+3
            took_area.append(area)
    need_number = criteria.man_general_area_num-len(took_area)
    if need_number <0: need_number = 0
    if(need_number>0):
        for area in criteria.man_general_area.split('|'):
            if area not in took_area:
                area_need.append(area)
    for lecture in lectures:
        general_credit = general_credit+3
    cds = []
    cds.append(criteria.science_credit-science_credit)
    cds.append(criteria.language_credit-language_credit)
    cds.append(criteria.major_credit-major_credit)
    cds.append(criteria.general_credit-general_credit)
    cds.append(criteria.total_credit - (major_credit+general_credit))
    for idx in range(0,len(cds)):
        if(cds[idx]<0):
            cds[idx]=0
    science_need = cds[0]
    language_need = cds[1]
    general_credit_need = science_need+language_need+3*len(math_need)+need_number*3
    if not sociality: general_credit_need = general_credit_need+3
    if not creativity: general_credit_need = general_credit_need+3
    message = grad_message(major_need,sociality==False,creativity==False,cds[0],#[0] => science need credit. [1] => language need credit
    cds[1],math_need,area_need,cds[2],general_credit_need,cds[4],major_credit,general_credit,(major_credit+general_credit))
    return message
