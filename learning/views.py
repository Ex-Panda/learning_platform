from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from learning.models import Course, Lesson, Pay
from learning.serializers import CourseSerializer, LessonSerializer, PaySerializer, MyTokenObtainPairSerializer


class ModeratorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.groups.filter(name='moderator').exists():
            return True


class ChecksUser:
    def get_object(self):
        #переопределяю метод, получаю объект, проверяю пользователя по требованиям
        self.object = super().get_object()
        if self.object.user != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object

    def get_queryset(self):
        # Модератор видит все курсы и уроки
        if self.request.user.groups.filter(name='moderator').exists() or self.request.user.is_superuser:
            qs = super().get_queryset()
            return qs
        # пользователь видит только свои курсы и уроки
        else:
            qs = super().get_queryset()
            return qs.filter(user=self.request.user)


class CourseViewSet(ChecksUser, viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'update', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [ModeratorPermission, IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # привязка создателя к курсу
        serializer.save()
        self.request.user.course_set.add(serializer.instance)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # привязка создателя к уроку
        serializer.save()
        self.request.user.lesson_set.add(serializer.instance)


class LessonListAPIView(ChecksUser, generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(ChecksUser, generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(ChecksUser, generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(ChecksUser, generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class PayListAPIView(generics.ListAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_filter = ['date_pay']
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
