# Generated by Django 4.0.3 on 2022-03-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecritic_site', '0003_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to='game_img'),
        ),
    ]
