# Generated by Django 3.1.7 on 2022-02-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('last_date', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
