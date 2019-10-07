from django.contrib.auth.models import User
from django.db import models
from django.conf import Settings
from django.utils import timezone


class Entrada(models.Model):
    entrada = models.CharField(max_length=100)
    valor = models.FloatField()
    descricao = models.TextField()
    data_entrada = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='Entrada')
    total_entrada = models.FloatField()

    

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
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='Saida')

    def salvar(self):
        self.data_saida = timezone.now()
        self.save()
   
    def __str__(self):
        return self.saida


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='Usuario')
    cpf = models.CharField(max_length=14)    
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    

    def __str__(self):
        return self.nome


class Familia(models.Model):
    nome = models.CharField(max_length=200)
    membro = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE, related_name='Familia'
    )

    def __str__(self):
        return self.nome
