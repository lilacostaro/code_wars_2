def calculo_inss(salario_base):
    base_inss_1 = 1212.00
    base_inss_2 = 2427.35
    base_inss_3 = 3641.03
    teto_inss = 7087.22
    porcentagem_teto = 0.14
    porcentagem_1 = 0.075
    porcentagem_2 = 0.09
    porcentagem_3 = 0.12

    if salario_base > teto_inss:
        desconto_total = 828.39
        faixa = porcentagem_teto
    elif salario_base > base_inss_3:
        desconto_faixa_4 = (salario_base - base_inss_3) * porcentagem_teto
        desconto_total = desconto_faixa_4 + 345.92
        faixa = porcentagem_teto
    elif salario_base > base_inss_2:
        desconto_faixa_3 = (salario_base - base_inss_2) * porcentagem_3
        desconto_total = desconto_faixa_3 + 200.28
        faixa = porcentagem_3
    elif salario_base > base_inss_1:
        desconto_faixa_2 = (salario_base - base_inss_1) * porcentagem_2
        desconto_total = desconto_faixa_2 + 90.90
        faixa = porcentagem_2
    elif salario_base > 0:
        desconto_total = salario_base * porcentagem_1
        faixa = porcentagem_1

    return (desconto_total, faixa)


def calculo_IRRF(salario_base, desconto_inss):
    base_irrf_1 = 1903.98
    base_irrf_2 = 2826.65
    base_irrf_3 = 3751.05
    base_irrf_4 = 4664.68
    faixa_1 = 0.075
    faixa_2 = 0.15
    faixa_3 = 0.225
    faixa_4 = 0.275
    valor_por_dependente = 189.59

    salario_base = salario_base - desconto_inss

    if salario_base > base_irrf_4:
        desconto_irrf = salario_base * faixa_4 - 869.36
    elif salario_base > base_irrf_3:
        desconto_irrf = (salario_base * faixa_3) - 636.13
    elif salario_base > base_irrf_2:
        desconto_irrf = (salario_base * faixa_2) - 354.80
    elif salario_base > base_irrf_1:
        desconto_irrf = (salario_base * faixa_1) - 142.8
    elif salario_base > 0:
        desconto_irrf = 0

    return desconto_irrf

def valor_comissao(salario_base, porcentagem=0):
    comissao = salario_base * porcentagem

    return comissao

def Faltas(salario_base, quantidade_faltas=0):
    valor = (salario_base / 30) * quantidade_faltas

    return valor

def Dados_Holerite(salario_base, porcentagem_comissao=0, qt_faltas=0):
    comissao = valor_comissao(salario_base, porcentagem_comissao)
    valor_salario = salario_base + comissao
    inss = calculo_inss(valor_salario)
    irrf = calculo_IRRF(valor_salario, inss[0])
    valor_faltas = Faltas(salario_base, qt_faltas)
    total_descontos = valor_faltas + inss[0] + irrf
    liquido = valor_salario - total_descontos
    fgts = valor_salario * 0.08

    return (comissao, valor_salario, inss[0], inss[1] * 100, irrf,
            valor_faltas, total_descontos, liquido, fgts)