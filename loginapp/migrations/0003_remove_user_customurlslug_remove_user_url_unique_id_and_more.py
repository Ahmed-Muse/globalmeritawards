# Generated by Django 4.2.20 on 2025-03-25 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_user_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='customurlslug',
        ),
        migrations.RemoveField(
            model_name='user',
            name='url_unique_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userbranch',
        ),
        migrations.RemoveField(
            model_name='user',
            name='usercompany',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userdepartment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userdivision',
        ),
    ]
