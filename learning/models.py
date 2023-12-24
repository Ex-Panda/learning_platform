from django.db import models
from django.db.models import CASCADE

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name_course = models.CharField(max_length=50, verbose_name='название курса')
    preview_course = models.ImageField(verbose_name='превью курса', **NULLABLE)
    description_course = models.TextField(verbose_name='описание курса')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name_course}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name_course',)


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=50, verbose_name='название урока')
    description_lesson = models.TextField(verbose_name='описание урока')
    preview_lesson = models.ImageField(verbose_name='превью урока', ** NULLABLE)
    url_video = models.CharField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, verbose_name='курс', on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('name_lesson',)


class Pay(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=CASCADE, **NULLABLE)
    date_pay = models.DateField(verbose_name='дата оплаты', auto_now_add=True)
    paid_course = models.ForeignKey(Course, verbose_name='оплаченный курс', on_delete=CASCADE, **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, verbose_name='оплаченный урок', on_delete=CASCADE, **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='метод оплаты')

    def __str__(self):
        return f'{self.date_pay}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=CASCADE, **NULLABLE)
    course_subscription = models.ForeignKey(Course, verbose_name='курс в подписке', on_delete=CASCADE)
