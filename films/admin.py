from django.contrib import admin
from .models import Genres,Trailer,Cast,Director,Episode,Writer,Detail
from django.utils.translation import gettext_lazy as _
# Register your models here.
admin.site.site_title = admin.site.site_header = 'Dashboard'
class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Genres,GenresAdmin)
admin.site.register(Trailer)

class CastAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Cast,CastAdmin)

class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Director,DirectorAdmin)

class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Episode,EpisodeAdmin)

class WriterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Writer,WriterAdmin)

class DetailAdmin(admin.ModelAdmin):
    search_fields = ('directors','casts','writers')
    list_display = ('name','created','watchDate','modified')
    list_filter = ('directors','casts','writers','genres','watchDate')
    prepopulated_fields = {'slug':('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'slug')}),
        (_('Movie info'), {'fields': ('genres','casts','directors','episodes','writers')}),
        (_('Movie is'), {'fields': ('status', 'hot')}),
        (_('Background'), {'fields': ('background', 'titleImage')}),
        (_('Important dates'), {'fields': ( 'watchDate',)}),
    )
    filter_horizontal = ('genres','casts','directors','episodes','writers')
admin.site.register(Detail,DetailAdmin)