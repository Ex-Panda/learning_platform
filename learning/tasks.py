from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone


from config import settings
from learning.models import Course
from users.models import User


@shared_task
def send_mail_user(user_id):
    user = User.objects.get(id=user_id)
    mail = send_mail(
        "Обновление курса!",
        "В вашем курсе обновлен материал, зайдите в личный кабинет",
        settings.EMAIL_HOST_USER,
        [user.email])


@shared_task
def check():
    courses = Course.objects.all()
    now = timezone.now()
    for course in courses:
        lesson = courses.lesson_set.last()
        if lesson.date_create == now.date():
            for subscription in course.subscription_set.all():
                send_mail_user.delay(subscription.user.id)


@shared_task
def last_login_user():
    now = timezone.now()
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login + timedelta(days=30) < now:
            user.is_active = False
            user.save()



