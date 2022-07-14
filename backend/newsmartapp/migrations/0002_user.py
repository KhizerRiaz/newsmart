# Generated by Django 4.0.4 on 2022-07-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmartapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, default='', max_length=100)),
                ('lastname', models.CharField(blank=True, default='', max_length=100)),
                ('DOB', models.DateField(blank=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]