# Generated by Django 3.0.3 on 2020-05-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0011_auto_20200524_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='image_name',
            field=models.CharField(max_length=50),
        ),
    ]
