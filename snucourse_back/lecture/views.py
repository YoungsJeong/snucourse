from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lecture, LectureOpinion
from .serializers import LectureOpinionSerializer,LectureSerializer
import json

@api_view(['GET'])
def lecture_detail(request, pk):
    try:
        lecture = Lecture.objects.get(pk=pk)
    except lecture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LectureSerializer(instance=lecture)
    if request.method == 'GET':
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def write_opinion(request):
    if request.method == 'POST':
        data = request.data
        serializer = LectureOpinionSerializer(data=data)
        if serializer.is_valid():
            opinion = serializer.save()
            request.user.lecture_opinions.add(opinion)

            lecture = Lecture.objects.get(pk=data.get('lecture'))
            count = LectureOpinion.objects.filter(lecture=lecture).count()
            lecture.easy = (lecture.easy*count+int(data['easy']))//(count)
            lecture.useful = (lecture.useful*count+int(data['useful']))//(count)
            lecture.credit = (lecture.credit*count+int(data['credit']))//(count)
            lecture.avg_review_score = (lecture.easy+lecture.useful+lecture.credit)/3
            lecture.save()

            return Response(serializer.data)
        return Response(data=serializer.errors)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lectureopinion_detail(request, pk):
    try:
        opinion = LectureOpinion.objects.get(pk=pk)
    except LectureOpinion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LectureOpinionSerializer(opinion)
        return Response(serializer.data)
    data = request.data
    if request.user != opinion.author: return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'PUT':
        serializer = LectureOpinionSerializer(opinion, data=request.data)
        if serializer.is_valid():
            lecture = Lecture.objects.get(pk=data['lecture'])
            count = LectureOpinion.objects.filter(lecture=lecture).count()
            lecture.easy = lecture.easy+(int(data['easy'])-opinion.easy)//count
            lecture.useful = lecture.useful+(int(data['useful'])-opinion.useful)//count
            lecture.credit = lecture.credit+(int(data['credit'])-opinion.credit)//count
            lecture.avg_review_score = (lecture.easy+lecture.useful+lecture.credit)/3
            opinion.easy = int(data['easy'])
            opinion.useful = int(data['useful'])
            opinion.credit = int(data['credit'])
            lecture.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lecture = Lecture.objects.get(pk=data['lecture'])
        count = LectureOpinion.objects.filter(lecture=lecture).count()
        lecture.easy = (lecture.easy*count - opinion.easy)/(count-1)
        lecture.useful = (lecture.useful*count - opinion.useful)/(count-1)
        lecture.credit = (lecture.credit*count - opinion.credit)/(count-1)
        lecture.avg_review_score = (lecture.easy+lecture.useful+lecture.credit)/3
        lecture.save()
        opinion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
