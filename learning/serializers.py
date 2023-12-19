from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from learning.models import Course, Lesson, Pay, Subscription
from learning.validators import TitleValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [TitleValidator(field='description_lesson'), TitleValidator(field='url_video')]


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.IntegerField(source='lesson_set.all.count', read_only=True)
    lesson = LessonSerializer(source='lesson_set', read_only=True, many=True)

    class Meta:
        model = Course
        fields = "__all__"
        validators = [TitleValidator(field='description_course')]

    @staticmethod
    def get_count_lesson(obj):
        return obj.lesson.count()


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['course_subscription']

