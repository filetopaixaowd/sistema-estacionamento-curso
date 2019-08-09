from django.contrib import admin
from .models import Marca, Veiculos, Pessoa, Parametros, MovRotativo, Mensalista, MovMensalista



class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total', 'horas_total')

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pago', 'total')

# class VeiculoApp(admin.ModelAdmin):
#     list_display = ('nome', 'placa', 'proprietario')
#     search_fields = ("proprietario__nome",)



admin.site.register(Marca)
admin.site.register(Veiculos)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)