# Generated by Django 2.1 on 2021-06-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210606_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
