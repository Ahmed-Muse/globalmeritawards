# Generated by Django 4.2.20 on 2025-03-22 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('comments', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompaniesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('comments', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('votes', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='awards.categoriesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='VotesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='awards.companiesmodel')),
                ('voter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='category',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='company',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voter',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
