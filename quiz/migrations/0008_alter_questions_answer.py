# Generated by Django 3.2.8 on 2021-11-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_quiz_pass_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=26),
        ),
    ]