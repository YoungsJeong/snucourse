from lecture.models import Lecture,LectureName
from user.models import GraduateCriteria,College,Department
import graduate
'''
lecs = ['대학영어 2: 글쓰기','수학 및 연습 1','물리학 1','컴퓨터의 개념 및 실습','통계학','물리학실험 1',
'물리학실험 2','통계학실험','글쓰기의 기초','수학 및 연습 2','물리학 2','생물학','생물학실험','공학수학 1','한국음악의 이해',
'디지털아트공학','구조정역학','선박계산','해양열전기기초','고급영어: 문화와 사회','공학수학 2','구조동역학','컴퓨터이용선형설계',
'역사 속의 전쟁과 평화','신호처리','선박해양유체역학','이산수학','컴퓨터구조','공학인을 위한 경영','유체역학기초','해양파역학',
'전기전자회로','알고리즘','동서양 명작 읽기','자료구조','화학','화학실험','논리설계','소프트웨어응용','현대종교와 문화','선박해양창의설계',
'하드웨어시스템설계','IT-리더십세미나','컴퓨터프로그래밍']
'''
lecs = []
lectures =[]
for lecture in lecs:
	ln = LectureName.objects.filter(name=lecture).all()
	if(ln.count()!=0):
		lectures.append(ln[0])
criteria = GraduateCriteria.objects.all()[0]
message = graduate.toMessage(lectures,criteria)
print(message.toJSON())