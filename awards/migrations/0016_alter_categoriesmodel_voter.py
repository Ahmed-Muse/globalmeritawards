# Generated by Django 4.2.20 on 2025-03-29 18:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0015_alter_votesmodel_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriesmodel',
            name='voter',
            field=models.ManyToManyField(blank=True, related_name='votercategories', to=settings.AUTH_USER_MODEL),
        ),
    ]
