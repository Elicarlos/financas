from django.contrib.auth.models import User
from django.db import models
from django.conf import Settings
from django.utils import timezone


class Entrada(models.Model):
    entrada = models.CharField(max_length=100)
    valor = models.FloatField()
    descricao = models.TextField()
    data_entrada = models.DateField(blank=True, null=True)

    def salvar(self):
        self.data_entrada = timezone.now()
        self.save()

    def __str__(self):
        return self.entrada


class Saida(models.Model):
    saida = models.CharField(max_length=100)
    valor = models.FloatField()
    descricao = models.TextField()
    data_saida = models.DateField()

    def salvar(self):
        self.data_saida = timezone.now()
        self.save()
   
    def __str__(self):
        return self.saida


class Usuario(models.Model):
    cpf = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Usuario')    
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Familia(models.Model):
    nome = models.CharField(max_length=200)
    parentesco = models.CharField(max_length=100)
    membro = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE, related_name='Familia'
    )

    def __str__(self):
        return self.nome
