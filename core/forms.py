from django.forms import ModelForm
from .models import Pessoa, Veiculos, MovRotativo, Mensalista, MovMensalista

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculos
        fields = '__all__'

class MovRotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

class MovMesForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'