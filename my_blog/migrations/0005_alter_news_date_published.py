# Generated by Django 4.1.7 on 2023-09-16 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_alter_news_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 16, 17, 53, 17, 966118, tzinfo=datetime.timezone.utc)),
        ),
    ]