# Generated by Django 4.2.13 on 2024-09-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refs', '0004_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
