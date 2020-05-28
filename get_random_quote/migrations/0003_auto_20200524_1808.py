# Generated by Django 3.0.3 on 2020-05-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0002_quote_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='quote',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
