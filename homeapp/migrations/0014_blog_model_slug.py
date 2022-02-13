# Generated by Django 4.0.2 on 2022-02-12 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0013_blog_model_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_model',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]