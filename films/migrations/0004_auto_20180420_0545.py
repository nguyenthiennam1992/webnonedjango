# Generated by Django 2.0.4 on 2018-04-19 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_genres_disable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genres',
            options={'verbose_name': 'Genres', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='trailer',
            options={'verbose_name': 'Trailer', 'verbose_name_plural': 'Trailer'},
        ),
    ]
