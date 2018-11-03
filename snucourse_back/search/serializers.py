from rest_framework import serializers
from lecture.models import Lecture, LectureName
from user.models import Department


class DepartmentSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class LectureNameSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id']

    def to_representation(self, instance):
        data = super(LectureNameSearchSerializer, self).to_representation(instance)

        data.update({
            'name': LectureName.objects.get(id=data['id']).name
        })

        return data


class LectureSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

    def to_representation(self, instance):
        data = super(LectureSearchSerializer, self).to_representation(instance)

        data.update({
            'name': LectureName.objects.get(id=instance.name.id).name,
            'department': Department.objects.get(id=instance.department.id).name
        })

        return data



