# Generated by Django 4.2.5 on 2023-09-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_search_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]