# Generated by Django 4.0.2 on 2022-02-12 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0017_blog_model_skill_des_blog_model_how_to_apply_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_model',
            old_name='des',
            new_name='content',
        ),
    ]