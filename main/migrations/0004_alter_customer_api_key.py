# Generated by Django 3.2.5 on 2021-09-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_visitor_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='api_key',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]