from django.contrib import admin
from .models import Genres,Trailer,Cast,Director,Episode,Writer,Detail,Notaion
from django.utils.translation import gettext_lazy as _
# Register your models here.
admin.site.site_title = admin.site.site_header = 'Dashboard'
class GenresAdmin(admin.ModelAdmin):
    search_fields = ('name','slug')
    list_display = ('name','slug','details','disable')
    list_filter = ('name','slug',)
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Genres,GenresAdmin)

class CastAdmin(admin.ModelAdmin):
    search_fields = ('name','slug','nation','sex','birth')
    list_display = ('name','slug','nation','isstar')
    list_filter = ('name','slug','nation','isstar')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Cast,CastAdmin)

class DirectorAdmin(admin.ModelAdmin):
    search_fields = ('name','slug','sex','birth')
    list_display = ('name','slug','sex','birth')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Director,DirectorAdmin)

class EpisodeAdmin(admin.ModelAdmin):
    search_fields = ('name','slug','released')
    list_display = ('name','slug','desciption','time','released')
    list_filter = ('name','slug','time','released')
    prepopulated_fields = {'slug':('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'slug','desciption')}),
        (_('Episode data'), {'fields': ('urlData','titleImage')}),
        (_('Important dates'), {'fields': ( 'released',)}),
    )
admin.site.register(Episode,EpisodeAdmin)

class WriterAdmin(admin.ModelAdmin):
    search_fields = ('name','slug')
    list_display = ('name','slug')
    list_filter = ('name','slug')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Writer,WriterAdmin)

class TrailerAdmin(admin.ModelAdmin):
    search_fields = ('name','slug')
    list_display = ('name','slug','urlData','watchDate')
    list_filter = ('name','slug','watchDate')
    prepopulated_fields = {'slug':('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'slug')}),
        (_('Trailer info'), {'fields': ('urlData','background')}),
        (_('Important dates'), {'fields': ( 'watchDate',)}),
    )
admin.site.register(Trailer,TrailerAdmin)

class DetailAdmin(admin.ModelAdmin):
    search_fields = ('directors','casts','writers')
    list_display = ('name','created','watchDate','modified')
    list_filter = ('directors','casts','writers','genres','watchDate')
    prepopulated_fields = {'slug':('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'slug','rating')}),
        (_('Movie info'), {'fields': ('genres','trailer','episodes')}),
        (_('Person'),{'fields':('casts','directors','writers')}),
        (_('Movie is'), {'fields': ('status', 'hot')}),
        (_('Background'), {'fields': ('background', 'titleImage')}),
        (_('Important dates'), {'fields': ( 'watchDate',)}),
    )
    filter_horizontal = ('genres','casts','trailer','directors','episodes','writers')
admin.site.register(Detail,DetailAdmin)

class NotaionAdmin(admin.ModelAdmin):
    search_fields = ('name','slug')
    list_display = ('name','slug')
    list_filter = ('name','slug','region')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Notaion,NotaionAdmin)