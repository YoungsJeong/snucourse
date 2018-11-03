from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import DepartmentSearchSerializer, LectureNameSearchSerializer, LectureSearchSerializer
from lecture.models import LectureName, Lecture
from user.models import Department
from haystack.query import SearchQuerySet


@api_view(['GET'])
def search_lecture_name(request):
    q = request.GET.get('q', '')
    if q is '':
        return Response(data=[], status=status.HTTP_200_OK)
    sqs = SearchQuerySet().models(LectureName).filter(name__contains=q)

    if len(sqs) == 0:
        sqs = SearchQuerySet().models(LectureName).autocomplete(autocomplete_search=q)

    serializer_list = []

    for sqs_element in sqs:
        lecture = Lecture.objects.get(id=sqs_element.object.id)
        serializer_list.append(lecture)

    serializer = LectureNameSearchSerializer(serializer_list, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_department(request):
    q = request.GET.get('q', '')
    if q is '':
        return Response(data=[], status=status.HTTP_200_OK)
    sqs = SearchQuerySet().models(Department).filter(name__contains=q)

    if len(sqs) == 0:
        sqs = SearchQuerySet().models(Department).autocomplete(autocomplete_search=q)

    serializer_list = []

    for sqs_element in sqs:
        department = Department.objects.get(id=sqs_element.object.id)
        serializer_list.append(department)

    serializer = DepartmentSearchSerializer(serializer_list, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_lecture_detail(request):
    qs = request.GET
    if len(qs) == 0:
        return Response(data=[], status=status.HTTP_200_OK)

    sqs = SearchQuerySet().models(Lecture)
    for q in qs:
        if q == 'name':
            sqs = sqs.filter_and(name__contains=qs[q])
        if q == 'type':
            sqs = sqs.filter_and(type__contains=qs[q])
        if q == 'department':
            sqs = sqs.filter_and(department__contains=qs[q])
        if q == 'area':
            sqs = sqs.filter_and(area__contains=qs[q])
        if q == 'lecturer':
            sqs = sqs.filter_and(lecturer__contains=qs[q])
        if q == 'credit_Total':
            sqs = sqs.filter_and(credit_Total=int(qs[q]))
        if q == 'grade':
            sqs = sqs.filter_and(grade=qs[q])
    serializer_list = []

    for sqs_element in sqs:
        lecture = Lecture.objects.get(id=sqs_element.object.id)
        serializer_list.append(lecture)

    serializer = LectureSearchSerializer(serializer_list, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
