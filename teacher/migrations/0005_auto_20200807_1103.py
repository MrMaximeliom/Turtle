# Generated by Django 3.0.8 on 2020-08-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20200718_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_period',
            field=models.CharField(max_length=250, verbose_name='exam period'),
        ),
    ]