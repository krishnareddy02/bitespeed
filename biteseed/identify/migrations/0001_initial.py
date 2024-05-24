# Generated by Django 5.0.6 on 2024-05-22 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField()),
                ('phoneNumber', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('linkedId', models.IntegerField()),
                ('linkPrecedence', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(default=datetime.datetime.now)),
                ('updatedAt', models.DateTimeField(default=datetime.datetime.now)),
                ('deletedAt', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]