# Generated by Django 3.0.6 on 2020-07-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_full_mark',
            field=models.IntegerField(verbose_name='exam full mark'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_pass_mark',
            field=models.IntegerField(verbose_name='exam pass mark'),
        ),
    ]