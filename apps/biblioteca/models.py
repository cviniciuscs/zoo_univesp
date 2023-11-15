from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Livro(models.Model):

    OPCAO_CATEGORIA = [
        ("LITERATURA INFANTIL", "Literatura Infantil"),
        ("LITERATURA JUVENIL", "Literatura Juvenil"),
        ("FICÇÃO", "Ficção"),
        ("AUTOBIOGRAFIA", "Autobiografia"),
        ]

    animal = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False, default=None)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCAO_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    emprestado = models.BooleanField(default=False)
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
