from haystack import indexes
from lecture.models import LectureName, Lecture
from user.models import Department


class LectureNameIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    name = indexes.CharField(model_attr='name')

    autocomplete_search = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return LectureName

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class DepartmentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    name = indexes.CharField(model_attr='name')

    autocomplete_search = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Department

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class LectureIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    name = indexes.MultiValueField()  # 강의이름
    type = indexes.CharField(model_attr='type')  # 교과구분
    department = indexes.MultiValueField()  # 개설학과
    area = indexes.CharField(model_attr="area")  # 교양영역
    lecturer = indexes.CharField(model_attr="lecturer")  # 담당교수
    credit_Total = indexes.IntegerField(model_attr="credit_Total")  # 총학점
    grade = indexes.CharField(model_attr="grade")  # 학년

    def get_model(self):
        return Lecture

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    def prepare_department(self, obj):
        return Lecture.objects.get(id=obj.id).department.name

    def prepare_name(self, obj):
        return Lecture.objects.get(id=obj.id).name.name
