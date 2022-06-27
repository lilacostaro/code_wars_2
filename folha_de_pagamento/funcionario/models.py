from django.db import models

# Create your models here.

class Cargo(models.Model):
    codigo = models.CharField(max_length=2, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=256, null=False, blank=False)
    salario_base = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    comissao = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f'{self.codigo}'

class Funcionario(models.Model):
    matricula = models.CharField(max_length=6, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=256, null=False, blank=False)
    CPF = models.CharField(max_length=14, null=False, blank=False, unique=True)
    data_admissao = models.DateField(null=False, blank=False)
    cargo_id = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    comissao = models.BooleanField(default=False, null=False, blank=False)

class Holerite(models.Model):
    mes_referencia = models.CharField(max_length=20)
    matricula = models.CharField(max_length=6)
    nome = models.CharField(max_length=256)
    data_adimissao = models.DateField(null=False, blank=False)
    cargo_nome =
    salario_base
    comissão
    faltas
    inss_folha
    irrf_folha
    total_vencimentos
    total_descontos
    fgts
    base_irrf
    liquido_receber

