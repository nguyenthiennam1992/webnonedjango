from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.db.models.manager import EmptyManager
from django.utils import timezone
# Create your models here.
class GenresManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)
class Genres(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    details = models.TextField(max_length=1000)
    disable = models.BooleanField(
        _('Hide Genres'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    objects = GenresManager()
    class Meta:
        verbose_name = _('Genres')
        verbose_name_plural = _('Genres')
    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

class Trailer(models.Model):
    urlData = models.URLField(max_length=1000)
    background = models.URLField(max_length=1000)
    slug = models.SlugField(max_length=40)
    # objects = TrailerManager()
    class Meta:
        verbose_name = _('Trailer')
        verbose_name_plural = _('Trailer')
    def __str__(self):
        return self.slug

class CastManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)
class Cast(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    objects = CastManager()
    def __str__(self):
        return self.name
    def natural_key(self):
        return (self.name,)

class DirectorManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)
class Director(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    objects = DirectorManager()
    def __str__(self):
        return self.name
    def natural_key(self):
        return (self.name,)

class EpisodeManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)
class Episode(models.Model):
    name = models.CharField(max_length=255)
    desciption = models.TextField(max_length=1000)
    urlData = models.URLField(max_length=1000)
    slug = models.SlugField(max_length=40)
    time = models.IntegerField
    objects = EpisodeManager()
    def __str__(self):
        return self.name
    def natural_key(self):
        return (self.name,)

class WriterManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)
class Writer(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    objects = WriterManager()
    def __str__(self):
        return self.name 
    def natural_key(self):
        return (self.name,)

class Detail(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    directors = models.ManyToManyField(Director, verbose_name=_('Director'),help_text=_(
            'Film dorector, click text to add list here '
            'click remove all/add all clear list/add full list'
        ),)
    casts = models.ManyToManyField(Cast,verbose_name=_('Cast'),help_text=_(
            ' The actors in this film, click text to add list here '
            'click remove all/add all clear list/add full list'
        ),)
    writers = models.ManyToManyField(Writer,verbose_name=_('Writer'),help_text=_(
            ' The Writer, click text to add list here '
            'click remove all/add all clear list/add full list'
        ),)
    genres = models.ManyToManyField(Genres,verbose_name=_('genres'),help_text=_(
            ' The genres, click text to add list here '
            'click remove all/add all clear list/add full list'
        ),)
    episodes = models.ManyToManyField(Episode,verbose_name=_('Episode'),help_text=_(
            'Episode list, click text to add list here '
            'click remove all/add all clear list/add full list'
        ),)
    background = models.URLField(max_length=1000)
    titleImage = models.URLField(max_length=1000)
    status = models.BooleanField(
         _('Status'),
        default=False,
        help_text=_(
            'The movie hide/show '
            'You cant click it'
        ),
    )
    hot = models.BooleanField(
         _('Is hot'),
        default=False,
        help_text=_(
            'The movie is Good/normal '
            'If checked is good.'
        ),
    )
    created = models.DateTimeField(_('date created'), default=timezone.now)
    watchDate = models.DateTimeField(_('date puslish'), default=timezone.now)
    modified = models.DateTimeField(_('date joined'), default=timezone.now)
    def __str__(self):
        return self.name