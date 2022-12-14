from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.
class VersionAppAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VersionApp._meta.get_fields()]
    search_fields = ['version', 'date_version']

class HistoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StockHistory._meta.get_fields()]
    search_fields = ['date_historique']


@admin.register(ModelePompe, StockPompe, Fabriquant, Doc, Site, Batiment, Etage, Piece, ModelEquipe, Huile, PiecesPompe,
                Tutelle, Inventaire, Kit, TechnologiePompe)
@admin.display(description= 'nom')
class PersonAdmin(ImportExportModelAdmin):
    pass

admin.site.register(VersionApp, VersionAppAdmin),
admin.site.register(StockHistory, HistoryAdmin)