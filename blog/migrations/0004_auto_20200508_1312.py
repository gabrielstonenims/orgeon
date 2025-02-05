# Generated by Django 3.0.6 on 2020-05-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200508_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfoprogress',
            name='client_image',
            field=models.ImageField(blank=True, upload_to='client_images'),
        ),
        migrations.AlterField(
            model_name='clientinfoprogress',
            name='email',
            field=models.EmailField(blank=True, help_text="Leave blank if client doesn't have any.", max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='clientinfoprogress',
            name='emergency_phone',
            field=models.CharField(blank=True, help_text="Leave blank if client doesn't have any.", max_length=20),
        ),
        migrations.AlterField(
            model_name='clientinfoprogress',
            name='next_of_kin',
            field=models.CharField(blank=True, help_text="Leave blank if client doesn't have any.", max_length=50),
        ),
        migrations.AlterField(
            model_name='clientinfoprogress',
            name='progress',
            field=models.CharField(choices=[('Accessment', 'Accessment'), ('Development', 'Development'), ('Planning', 'Planning'), ('Implementation', 'Implementation'), ('Evaluation', 'Evaluation'), ('Star', 'Star')], default='Accessment', help_text='Choose current level for your client.', max_length=30),
        ),
    ]
