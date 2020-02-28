# Generated by Django 3.0.3 on 2020-02-28 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200228_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ImageField(blank=True, help_text='Leave this field blank if message has no image.', upload_to='post_posters', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg'])]),
        ),
    ]