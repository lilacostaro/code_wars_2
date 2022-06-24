from django.contrib import admin
from .models import Cargo, Funcionario
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'salario_base', 'comissao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'comissao')