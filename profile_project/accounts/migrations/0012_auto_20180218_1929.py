# Generated by Django 2.0.1 on 2018-02-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180218_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_animal',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobby',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='', max_length=255),
        ),
    ]
