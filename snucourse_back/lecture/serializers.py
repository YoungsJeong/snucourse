from rest_framework import serializers
from .models import LectureOpinion, Lecture, LectureName

class LectureOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureOpinion
        fields = '__all__'

    def to_representation(self, instance):
        data = super(LectureOpinionSerializer, self).to_representation(instance)

        data.update({
            "lecture": {}
        })

        data['lecture'].update({
            'credit_Total': instance.lecture.credit_Total,
            'name': instance.lecture.name.name,
            'lecturer': instance.lecture.lecturer,
            'grade': instance.lecture.grade,
            'type':instance.lecture.type,
            'easy':instance.lecture.easy,
            'credit':instance.lecture.credit,
            'useful':instance.lecture.useful,
            "avg_review_score": instance.lecture.avg_review_score,
        })

        return data


class LectureSerializer(serializers.ModelSerializer):
    lectureopinion_set = LectureOpinionSerializer(many=True, read_only=True)

    def get_lectureopinion_set(self, obj):
        print(obj.lectureopinion_set.all())
        return obj.lectureopinion_set

    class Meta:
        model = Lecture
        fields = '__all__'

    def to_representation(self, instance):
        data = super(LectureSerializer, self).to_representation(instance)
        data.update({
            'name': LectureNameSerializer(instance.name).data['name'],
            'department': instance.department.name,
        })

        return data


class LectureNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureName
        fields = '__all__'
