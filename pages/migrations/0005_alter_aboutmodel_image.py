# Generated by Django 5.0.2 on 2024-02-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_aboutmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about_images/'),
        ),
    ]
