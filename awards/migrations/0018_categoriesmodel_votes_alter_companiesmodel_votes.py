# Generated by Django 4.2.20 on 2025-03-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0017_alter_companiesmodel_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesmodel',
            name='votes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='companiesmodel',
            name='votes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
