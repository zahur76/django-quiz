# Generated by Django 3.2.8 on 2021-11-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20211106_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='pass_mark',
            field=models.IntegerField(default=75),
        ),
    ]