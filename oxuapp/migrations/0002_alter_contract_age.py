# Generated by Django 4.2.7 on 2023-12-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oxuapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
