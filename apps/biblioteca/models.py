from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Livro(models.Model):

    OPCAO_CATEGORIA = [
        ("AVE", "Ave"),
        ("MAMÍFERO", "Mamífero"),
        ("RÉPTIL", "Réptil"),
        ("ANFÍBIO", "Anfíbio"),
        ]

    OPCAO_SEXO = [
        ("MASCULINO", "Masculino"),
        ("FEMININO", "Feminino"),
        ("INDETERMINADO", "Indeterminado"),
        ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    especie = models.CharField(max_length=100, null=False, blank=False, default=None)
    nome_popular = models.CharField(max_length=150, null=False, blank=False)
    classe = models.CharField(max_length=100, choices=OPCAO_CATEGORIA, default="")
    observação = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    sexo = models.CharField(max_length=100, choices=OPCAO_SEXO, default="")
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user'
        )

    def __str__(self):
        return self.nome
