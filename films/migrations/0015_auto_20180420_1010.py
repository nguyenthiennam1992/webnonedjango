# Generated by Django 2.0.4 on 2018-04-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0014_auto_20180420_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='casts',
            field=models.ManyToManyField(help_text=' The actors in this film, click text to add list here click remove all/add all clear list/add full list', to='films.Cast', verbose_name='Cast'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='directors',
            field=models.ManyToManyField(help_text='Film dorector, click text to add list here click remove all/add all clear list/add full list', to='films.Director', verbose_name='Director'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='episodes',
            field=models.ManyToManyField(help_text='Episode list, click text to add list here click remove all/add all clear list/add full list', to='films.Episode', verbose_name='Episode'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='genres',
            field=models.ManyToManyField(help_text=' The genres, click text to add list here click remove all/add all clear list/add full list', to='films.Genres', verbose_name='genres'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='writers',
            field=models.ManyToManyField(help_text=' The Writer, click text to add list here click remove all/add all clear list/add full list', to='films.Writer', verbose_name='Writer'),
        ),
    ]
