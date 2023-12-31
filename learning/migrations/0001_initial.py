# Generated by Django 5.0 on 2023-12-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=50, verbose_name='название курса')),
                ('preview_course', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью курса')),
                ('description_course', models.TextField(verbose_name='описание курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
                'ordering': ('name_course',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=50, verbose_name='название урока')),
                ('description_lesson', models.TextField(verbose_name='описание урока')),
                ('preview_lesson', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью урока')),
                ('url_video', models.CharField(verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
                'ordering': ('name_lesson',),
            },
        ),
    ]
