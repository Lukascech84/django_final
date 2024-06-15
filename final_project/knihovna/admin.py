from django.contrib import admin
from .models import Uzivatel, Zanr, Vyvojar, Vydavatel, Hra


class UzivatelAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni")


admin.site.register(Uzivatel, UzivatelAdmin)
admin.site.register(Zanr)
admin.site.register(Vyvojar)
admin.site.register(Vydavatel)
admin.site.register(Hra)