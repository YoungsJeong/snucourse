from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserSerializer, UserDetailSerializer
from .models import GraduateCriteria
from lecture.models import LectureName, Lecture
from lecture.serializers import LectureSerializer
from user import graduate
import random


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid() and 'password' in data:
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)

            lectures = ['대학영어 2: 글쓰기', '수학 및 연습 1', '물리학 1', '컴퓨터의 개념 및 실습', '통계학', '물리학실험 1',
                    '통계학실험', '글쓰기의 기초', '생물학', '생물학실험', '해양열전기기초', '고급영어: 문화와 사회', '공학수학 2', '구조동역학', '컴퓨터구조',
                    '알고리즘', '자료구조', '화학', '화학실험', '논리설계', '소프트웨어응용', 'IT-리더십세미나', '컴퓨터프로그래밍']
            graduate_criteria = GraduateCriteria.objects.all()[0]

            user.graduate_criteria.add(graduate_criteria)
            for lecture_name in lectures:
                lecture = LectureName.objects.get(name=lecture_name)
                user.lectures.add(lecture)

            return Response(data={'token': token.key, 'user_name': user.name}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key, 'user_name': user.name}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_lectures(request):
    user = request.user
    if user.is_anonymous:
        return Response('Anonymous user is not allowed', status=status.HTTP_400_BAD_REQUEST)
    lecture_ids = request.data['lectures']

    for lecture_id in lecture_ids:
        if not LectureName.objects.filter(id=lecture_id).exists():
            return Response('Lecture is not exist', status=status.HTTP_400_BAD_REQUEST)

        lecture = LectureName.objects.get(id=lecture_id)
        user.lectures.add(lecture)

    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_info(request):
    user = request.user
    if user.is_anonymous:
        return Response('Anonymous user is not allowed', status=status.HTTP_400_BAD_REQUEST)

    return Response(data=UserDetailSerializer(user).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def check_graduate(request):
    if request.method == 'GET':
        user = request.user

        data = {
            'majors': [],
            'generals': [],
        }
        # for in case user is CS 2015
        message = graduate.toMessage(user.lectures, GraduateCriteria.objects.get(year=int(str(user.student_id)[:4])))

        # majors
        if len(message.major_need) != 0:
            for major_name in message.major_need:
                filtered_lecture = Lecture.objects.filter(name__name=major_name)
                if filtered_lecture.exists():
                    lecture = filtered_lecture[random.randrange(0, len(filtered_lecture))]
                    data['majors'].append(LectureSerializer(lecture).data)

        data['majors'] = sorted(data['majors'], key=lambda major: int(major['grade'][0]))

        # generals
        # regard math as general
        if len(message.math_need) != 0:
            for general_name in message.math_need:
                filtered_lecture = Lecture.objects.filter(name__name=general_name)
                if filtered_lecture.exists():
                    lecture = filtered_lecture[random.randrange(0, len(filtered_lecture))]
                    data['generals'].append(LectureSerializer(lecture).data)

        data['generals'] = sorted(data['generals'], key=lambda general: int(general['grade'][0]))

        data.update({
            "creativity_need": message.creativity_need,
            "general_credit_need": len(message.math_need) * 3,
            "language_need": message.language_need,
            "major_credit_need": message.major_credit_need,
            "science_need": message.science_need,
            "sociality_need": message.sociality_need,
            "total_credit_need": message.total_credit_need,
            "took_major_credit": message.took_major_credit,
            "took_general_credit": message.took_general_credit,
            "took_total_credit" : message.took_total_credit
        })

        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
