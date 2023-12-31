# Generated by Django 5.0 on 2023-12-24 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_alter_pay_date_pay_alter_pay_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='paid_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.course', verbose_name='оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='paid_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.lesson', verbose_name='оплаченный урок'),
        ),
    ]
