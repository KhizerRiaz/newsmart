# Generated by Django 4.0.4 on 2022-07-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmartapp', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
