# Generated by Django 3.0 on 2019-12-18 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsaudiences',
            old_name='read_on',
            new_name='recent_read_on',
        ),
        migrations.RenameField(
            model_name='notificationsaudiences',
            old_name='read_on',
            new_name='recent_read_on',
        ),
    ]