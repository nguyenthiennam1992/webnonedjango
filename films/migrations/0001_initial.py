# Generated by Django 2.0.4 on 2018-04-20 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import films.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=40)),
                ('isstar', models.BooleanField(default=False, help_text='The casr is star/normal You cant click it', verbose_name='Star')),
            ],
            managers=[
                ('objects', films.models.CastManager()),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=40)),
                ('rating', models.IntegerField(default=0)),
                ('background', models.URLField(max_length=1000)),
                ('titleImage', models.URLField(max_length=1000)),
                ('status', models.BooleanField(default=False, help_text='The movie hide/show You cant click it', verbose_name='Status')),
                ('hot', models.BooleanField(default=False, help_text='The movie is Good/normal If checked is good.', verbose_name='Is hot')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
                ('watchDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='released date')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('casts', models.ManyToManyField(help_text=' The actors in this film, click text to add list here click remove all/add all clear list/add full list', to='films.Cast', verbose_name='Cast')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=40)),
            ],
            managers=[
                ('objects', films.models.DirectorManager()),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desciption', models.TextField(max_length=1000)),
                ('urlData', models.URLField(max_length=1000)),
                ('titleImage', models.URLField(max_length=1000)),
                ('slug', models.SlugField(max_length=40)),
                ('time', models.IntegerField(default=0)),
                ('released', models.DateTimeField(default=django.utils.timezone.now, verbose_name='released date')),
            ],
            managers=[
                ('objects', films.models.EpisodeManager()),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=40)),
                ('details', models.TextField(max_length=1000)),
                ('disable', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Hide Genres')),
            ],
            options={
                'verbose_name': 'Genres',
                'verbose_name_plural': 'Genres',
            },
            managers=[
                ('objects', films.models.GenresManager()),
            ],
        ),
        migrations.CreateModel(
            name='Notaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=40)),
                ('region', models.IntegerField(choices=[(1, 'Asia'), (2, 'Asia'), (3, 'America'), (4, 'Africa'), (5, 'Australia'), (6, 'Antarctica'), (7, 'North America'), (8, 'South America')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('urlData', models.URLField(max_length=1000)),
                ('background', models.URLField(max_length=1000)),
                ('slug', models.SlugField(max_length=40)),
                ('watchDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='released date')),
            ],
            managers=[
                ('objects', films.models.TrailerManager()),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=40)),
            ],
            managers=[
                ('objects', films.models.WriterManager()),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='directors',
            field=models.ManyToManyField(help_text='Film dorector, click text to add list here click remove all/add all clear list/add full list', to='films.Director', verbose_name='Director'),
        ),
        migrations.AddField(
            model_name='detail',
            name='episodes',
            field=models.ManyToManyField(help_text='Episode list, click text to add list here click remove all/add all clear list/add full list', to='films.Episode', verbose_name='Episode'),
        ),
        migrations.AddField(
            model_name='detail',
            name='genres',
            field=models.ManyToManyField(help_text=' The genres, click text to add list here click remove all/add all clear list/add full list', to='films.Genres', verbose_name='genres'),
        ),
        migrations.AddField(
            model_name='detail',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Notaion'),
        ),
        migrations.AddField(
            model_name='detail',
            name='trailer',
            field=models.ManyToManyField(help_text='Chosen trailer for film click remove all/add all clear list/add full list', to='films.Trailer', verbose_name='Trailer'),
        ),
        migrations.AddField(
            model_name='detail',
            name='writers',
            field=models.ManyToManyField(help_text=' The Writer, click text to add list here click remove all/add all clear list/add full list', to='films.Writer', verbose_name='Writer'),
        ),
        migrations.AddField(
            model_name='cast',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Notaion'),
        ),
    ]
