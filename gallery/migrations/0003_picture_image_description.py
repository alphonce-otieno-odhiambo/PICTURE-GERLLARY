# Generated by Django 3.2.8 on 2021-11-28 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_picture_image_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]