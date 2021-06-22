from django.contrib import admin

from .models import Cargo, Servico, Equipe, Recursos


@admin.register(Cargo)
class CardoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')



@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado')


@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('nome',)
