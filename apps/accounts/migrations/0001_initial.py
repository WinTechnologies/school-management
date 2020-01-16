# Generated by Django 2.2 on 2020-01-16 16:23

import apps.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, validators=[apps.core.validators.validate_username])),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[apps.core.validators.validate_mobile])),
                ('device_token', models.CharField(blank=True, max_length=100, null=True)),
                ('channel_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_super_user', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
