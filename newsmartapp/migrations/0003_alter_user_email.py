# Generated by Django 4.0.4 on 2022-07-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmartapp', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
