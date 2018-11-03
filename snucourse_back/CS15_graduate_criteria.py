from user.models import College,Department,GraduateCriteria,User
from lecture.models import Lecture,LectureName


def tolist(list):
    from lecture.models import Lecture,LectureName
    ret = []
    for data in list:
        lec = LectureName.objects.filter(name=data)
        if(lec.count()!=0):
            ret.append(lec[0])
        elif('|' in data):
            ln = LectureName.objects.filter(name=data.split('|')[1])
            if(ln.count()!=0):
                lecture = Lecture.objects.filter(name=ln[0])  
                if(lecture.count()!=0):
                    temp = LectureName(name=data,credit=lecture[0].credit_Total)
                    temp.save()
                    ret.append(temp)
    return ret
department = Department.objects.filter(name='컴퓨터공학부')[0]
year = 2015
major_mandatories = ['이산수학','논리설계','컴퓨터프로그래밍','전기전자회로','자료구조','컴퓨터구조',
'소프트웨어 개발의 원리와 실제','시스템프로그래밍','하드웨어시스템설계','알고리즘','컴퓨터공학세미나|IT-리더십세미나',
'창의적통합설계1|창의적통합설계2']
major_optional = ['프로그래밍연습','정보통신융합','프로그래밍의 원리','오토마타이론','선형 및 비선형 계산모델','디지털신호처리',
'데이터마이닝 개론','운영체제','프로그래밍언어','IT벤처창업개론','데이터베이스','데이터통신','임베디드시스템과 응용','소프트웨어공학',
'인공지능','컴파일러','컴퓨터그래픽스','컴퓨터네트워크','컴퓨터엔지니어를 위한 기술 영어작문','소셜 네트워크 분석','컴퓨터시스템특강',
'소프트웨어응용','모바일 컴퓨팅과 응용','컴퓨터모델링','멀티코어 컴퓨팅','컴퓨터보안','웹정보시스템','컴퓨터융합응용','인간컴퓨터상호작용',
'기계학습 개론','영상처리','컴퓨터비전','컴퓨터 신기술 특강','인터넷 보안','경영학 원론','재무회계','회계원리','조직행위론','마케팅 관리',
'재무관리','인사관리','국제경영','현대경영이론','조직구조론','기술과 창업','현대기술과 윤리적 사고','공학기술의 역사','이노베이션과 창의력 실습',
'공학인을 위한 경영','창의공학설계','디지털아트공학','창의적 기술지능','공학도를 위한 창의적 사고','다학제 창의적 제품개발','글로벌 창의적 제품개발']
sociality = ['창업과 경제','기술과 경제','공학윤리와 리더십','특허와 기술창업','기술과 창업','현대기술과 윤리적 사고','공학기술의 역사','이노베이션과 창의력 실습',
'공학인을 위한 경영']
creativity = ['현대도시건축산책','창조와 디자인','테크놀러지와 예술: 전시예술공학','소리의 과학과 악기제작 체험','창의공학설계','디지털아트공학','창의적 기술지능',
'공학도를 위한 창의적 사고','다학제 창의적 제품개발','글로벌 창의적 제품개발']
science = ['기초물리학 1|물리학 1|고급물리학 1','기초물리학 2|물리학 2|고급 물리학 2','물리학','물리학실험','물리학실험 1','물리학실험 2',
'화학 1','화학 2','화학','화학실험 1','화학실험 2','화학실험','생물학 1','생물학 2','생물학','생물학실험','생물학실험 1','생물학실험 2']
science_credit = 12
language = []
lang = Lecture.objects.filter(area='학문의기초_외국어')
for lecture in lang:
    if lecture.name not in language:
        language.append(lecture.name)
language_credit = 4
math = ['글쓰기의 기초|과학과 기술 글쓰기','수학 및 연습 1|고급수학 및 연습1','수학 및 연습 2|고급 수학 및 연습2','공학수학 1','공학수학 2','통계학','통계학실험',
'컴퓨터의 개념 및 실습']
math_credit = 22
man_general_area = '문화와예술|언어와문학|역사와철학|인간과사회|정치와경제|'
man_general_area_num =2
major_credit = 63
general_credit = 44
total_credit = 130
CS15 = GraduateCriteria(department = department,year = year,science_credit=science_credit,language_credit=language_credit,
math_credit = math_credit, man_general_area = man_general_area,man_general_area_num=man_general_area_num,
major_credit= major_credit,general_credit = general_credit,total_credit=total_credit)
CS15.save()
CS15.major_mandatories.add(*tolist(major_mandatories))
CS15.major_optional.add(*tolist(major_optional))
CS15.sociality.add(*tolist(sociality))
CS15.creativity.add(*tolist(creativity))
CS15.science.add(*tolist(science))
CS15.language.add(*tolist(language))
CS15.math.add(*tolist(math))
