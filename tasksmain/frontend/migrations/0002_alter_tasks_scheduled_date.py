# Generated by Django 4.1.3 on 2023-11-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='scheduled_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
