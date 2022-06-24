from django.db import models

# Create your models here.

class Cargo(models.Model):
    codigo = models.CharField(max_length=2, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=256)
    salario_base = models.DecimalField(max_digits=8, decimal_places=2)
    comissao = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f'{self.codigo} - {self.nome}'

class Funcionario(models.Model):
    matricula = models.CharField(max_length=6, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=256, null=False, blank=False)
    CPF = models.CharField(max_length=14, null=False, blank=False)
    data_admissao = models.DateField()
    cargo_id = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    comissao = models.BooleanField(default=False)