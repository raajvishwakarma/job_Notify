# Generated by Django 4.0.2 on 2022-02-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_remove_card_model_apply_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
            ],
        ),
    ]