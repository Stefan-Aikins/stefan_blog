# Generated by Django 4.1.7 on 2023-09-16 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0005_alter_news_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
