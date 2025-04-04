# Generated by Django 4.2.20 on 2025-03-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0018_categoriesmodel_votes_alter_companiesmodel_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=25, null=True)),
                ('amount', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=1, default=0, max_digits=10, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
