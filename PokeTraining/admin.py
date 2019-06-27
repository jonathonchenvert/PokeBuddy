from django.contrib import admin

from .models import Pokemon, Attacks, Stats, OriginalTrainer

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Attacks)
admin.site.register(Stats)
admin.site.register(OriginalTrainer)
