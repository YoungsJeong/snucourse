from rest_framework import serializers
from .models import User, Department, College, GraduateCriteria
from lecture.serializers import LectureNameSerializer, LectureOpinionSerializer
from user import graduate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def to_representation(self, instance):
        data = super(DepartmentSerializer, self).to_representation(instance)
        data.update({
            'college': CollegeSerializer(instance.college).data
        })

        return data


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_active', 'is_staff', 'last_login', 'groups', 'user_permissions', 'graduate_criteria']

    def to_representation(self, instance):
        data = super(UserDetailSerializer, self).to_representation(instance)

        message = graduate.toMessage(instance.lectures.all(), GraduateCriteria.objects.get(year=int(str(instance.student_id)[:4])))
        data.update({
            'major': DepartmentSerializer(instance.major).data,
            'minor': DepartmentSerializer(instance.minor).data,
            'double_major': DepartmentSerializer(instance.double_major).data,
            'lectures': LectureNameSerializer(list(instance.lectures.all()), many=True).data,
            "creativity_need": message.creativity_need,
            "general_credit_need": message.general_credit_need,
            "language_need": message.language_need,
            "major_credit_need": message.major_credit_need,
            "science_need": message.science_need,
            "sociality_need": message.sociality_need,
            "total_credit_need": message.total_credit_need,
            "took_major_credit": message.took_major_credit,
            "took_general_credit": message.took_general_credit,
            "took_total_credit": message.took_total_credit,
            "lecture_opinions": LectureOpinionSerializer(list(instance.lecture_opinions.all()), many=True).data,
        })

        return data
