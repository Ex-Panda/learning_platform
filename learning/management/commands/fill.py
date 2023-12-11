from django.core.management import BaseCommand

from learning.models import Course, Lesson, Pay
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='test@gmail.com',
            first_name='test',
            last_name='testov',
            is_active=True
        )

        user.set_password('123qwe')
        user.save()

        course = Course.objects.all().first()
        lesson = Lesson.objects.filter(course=course).first()

        pay_list = [
            {'user': user, 'date_pay': '2023-12-11', 'paid_course': course, 'paid_lesson': lesson, 'payment_amount': 1000, 'payment_method': 'cash'},
            {'user': user, 'date_pay': '2023-12-11', 'paid_course': course, 'paid_lesson': lesson, 'payment_amount': 500, 'payment_method': 'cash'},
            {'user': user, 'date_pay': '2023-12-11', 'paid_course': course, 'paid_lesson': lesson, 'payment_amount': 200, 'payment_method': 'cash_less'},
            {'user': user, 'date_pay': '2023-12-11', 'paid_course': course, 'paid_lesson': lesson, 'payment_amount': 3000, 'payment_method': 'cash'}
        ]

        pay_for_create = []
        for pay_item in pay_list:
            pay_for_create.append(
                Pay(**pay_item)
            )

        Pay.objects.all().delete()
        Pay.objects.bulk_create(pay_for_create)

