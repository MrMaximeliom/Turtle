# Generated by Django 3.1 on 2020-10-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0015_remove_exam_encrypted_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='encrypted_id',
            field=models.BinaryField(blank=True, max_length=400, verbose_name='encrypted id'),
        ),
    ]
