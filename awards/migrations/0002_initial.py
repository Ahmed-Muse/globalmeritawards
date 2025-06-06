# Generated by Django 4.2.20 on 2025-05-22 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('awards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='votesmodel',
            name='voter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companiesmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categores', to='awards.categoriesmodel'),
        ),
        migrations.AddField(
            model_name='companiesmodel',
            name='voter',
            field=models.ManyToManyField(blank=True, related_name='votersusers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoriesmodel',
            name='voter',
            field=models.ManyToManyField(blank=True, related_name='votercategories', to=settings.AUTH_USER_MODEL),
        ),
    ]
