from django.urls import path

from learning.apps import LearningConfig
from rest_framework.routers import DefaultRouter

from learning.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PayListAPIView, MyTokenObtainPairView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView

app_name = LearningConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson', LessonListAPIView.as_view(), name='lessons'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('pay/', PayListAPIView.as_view(), name='pay'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('subscription/create', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
] + router.urls
