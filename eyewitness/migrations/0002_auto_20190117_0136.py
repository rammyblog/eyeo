# Generated by Django 2.1.5 on 2019-01-17 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyewitness', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank='True', unique=True),
        ),
    ]
