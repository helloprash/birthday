# Generated by Django 3.0.3 on 2020-05-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0009_auto_20200524_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
