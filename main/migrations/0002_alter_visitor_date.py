# Generated by Django 3.2.5 on 2021-09-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]