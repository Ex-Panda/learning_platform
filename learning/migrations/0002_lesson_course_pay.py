# Generated by Django 5.0 on 2023-12-11 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning.course', verbose_name='курс'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pay', models.DateField(verbose_name='дата оплаты')),
                ('payment_amount', models.IntegerField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(verbose_name='метод оплаты')),
                ('paid_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
