from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name_course = models.CharField(max_length=50, verbose_name='название курса')
    preview_course = models.ImageField(verbose_name='превью курса', **NULLABLE)
    description_course = models.TextField(verbose_name='описание курса')

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

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('name_lesson',)

