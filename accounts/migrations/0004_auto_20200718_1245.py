# Generated by Django 3.0.6 on 2020-07-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default_male.jpg', upload_to='profile_pics'),
        ),
    ]