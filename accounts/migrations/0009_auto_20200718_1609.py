# Generated by Django 3.0.8 on 2020-07-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200718_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default_male.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
