# Generated by Django 4.2.2 on 2023-06-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='facilitator',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='facilitator',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=250),
        ),
    ]
