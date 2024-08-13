from django.contrib import admin
from galeria.models import Fotografia

class AdminFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

admin.site.register(Fotografia, AdminFotografia)
