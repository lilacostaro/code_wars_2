from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import SingleObjectMixin
from .models import (Cargo,
                     Funcionario)

from .forms import AddEmployeeForm

from utils.funcoes_base import Dados_Holerite

# Create your views here.
def employeesList(request):
    employees_list = Funcionario.objects.order_by('nome')

    ultimo_id = Funcionario.objects.latest('matricula').matricula
    nova_matricula = 'px0002'

    context = {'employees_list': employees_list,
               'ultima_matricula': ultimo_id,
               'nova_matricula': nova_matricula}

    return render(request, 'funcionario/funcionario_lista.html', context)

def employeeInfo(request, matricula):
    funcionario = get_object_or_404(Funcionario, pk=matricula)
    id_cargo = funcionario.cargo_id
    cargo = get_object_or_404(Cargo, codigo=id_cargo)
    comissao_conf = cargo.comissao * 100

    context = {
        'cargo': cargo,
        'funcionario': funcionario,
        'comissao': comissao_conf
        }

    return render(request, 'funcionario/funcionario_info.html', context)

def gera_matricula():
    ultima_matricula = Funcionario.objects.latest('matricula').matricula

    numbers = int(ultima_matricula[2:])
    number = numbers + 1
    if len(str(number)) == 1:
        number = f'000{number}'
    elif len(str(number)) == 2:
        number = f'00{number}'
    elif len(str(number)) == 3:
        number = f'0{number}'
    elif len(str(number)) == 4:
        number = f'{number}'
    nova_matricula = 'PX' + number

    return nova_matricula


def addEmployee(request):
    if request.method == 'POST':
        form1 = AddEmployeeForm(request.POST)
        num_matricula = gera_matricula()

        if form1.is_valid():
            registro = form1.save(commit=False)
            registro.matricula = num_matricula
            registro.save()
            id = registro.matricula
            return redirect('employee_info', matricula=id)
    else:
        form1 = AddEmployeeForm()
        return render(request, 'funcionario/add_funcionario.html', {'form1': form1})


def gera_holerite(request, matricula):
    funcionario = get_object_or_404(Funcionario, pk=matricula)
    id_cargo = funcionario.cargo_id
    cargo = get_object_or_404(Cargo, codigo=id_cargo)

    salario_base_funcionario = cargo.salario_base
    if funcionario.comissao == True:
        porcentagem_comissao = cargo.comissao
    else:
        porcentagem_comissao = 0

    qt_faltas = 2
    mes_referencia = 'Janeiro'

    holerite_valores = Holerite(salario_base_funcionario, porcentagem_comissao, qt_faltas)

    comissao = holerite_valores[0]
    valor_salario = holerite_valores[1]
    inss_valor = holerite_valores[2]
    inss_porcentagem = holerite_valores[3]
    irrf = holerite_valores[4]
    valor_faltas = holerite_valores[5]
    total_descontos = holerite_valores[6]
    liquido = holerite_valores[7]
    fgts = holerite_valores[8]



