from rest_framework import serializers

from learning.models import Course, Lesson, Pay


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lesson = LessonSerializer(source='lesson_set', read_only=True, many=True)

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_count_lesson(obj):
        return obj.lesson.count()


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = "__all__"
