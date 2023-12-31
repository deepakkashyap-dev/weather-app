# Generated by Django 4.2.5 on 2023-09-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='keyword',
        ),
        migrations.AddField(
            model_name='search',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='humidity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='icon',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='temperature',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='wind',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
