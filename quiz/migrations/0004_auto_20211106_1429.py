# Generated by Django 3.2.9 on 2021-11-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0003_results"),
    ]

    operations = [
        migrations.AddField(
            model_name="results",
            name="attempts",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="results",
            name="results",
            field=models.CharField(default="0", max_length=254),
        ),
    ]
