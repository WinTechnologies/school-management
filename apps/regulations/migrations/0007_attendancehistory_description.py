# Generated by Django 2.2 on 2020-02-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulations', '0006_auto_20200129_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancehistory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
