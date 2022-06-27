from django import forms

from .models import Funcionario

class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ('matricula', 'nome', 'CPF', 'data_admissao', 'cargo_id', 'comissao')

