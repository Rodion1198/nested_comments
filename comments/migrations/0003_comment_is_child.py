# Generated by Django 3.2.3 on 2021-05-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
    ]
