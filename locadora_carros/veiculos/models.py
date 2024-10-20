# models.py
from django.db import models

class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)
    cor = models.CharField(max_length=30)
    preco_locacao = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"
