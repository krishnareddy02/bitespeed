# Generated by Django 5.0.6 on 2024-05-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='createdAt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='deletedAt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updatedAt',
            field=models.CharField(max_length=100),
        ),
    ]