# Generated by Django 4.2.20 on 2025-03-27 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0007_alter_companiesmodel_voter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votesmodel',
            name='voter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
