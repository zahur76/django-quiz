# Generated by Django 3.2.9 on 2021-11-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.IntegerField()),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Staff',
            },
        ),
    ]