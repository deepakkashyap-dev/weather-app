# Generated by Django 4.2.5 on 2023-09-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_search_keyword_search_city_search_humidity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='desc',
            field=models.CharField(max_length=255, null=True),
        ),
    ]