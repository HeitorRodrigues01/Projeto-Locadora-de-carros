from django.contrib import admin
from .models import Veiculo  

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "placa", "cor", "preco_locacao", "disponibilidade",)

admin.site.register(Veiculo, VeiculoAdmin)  
