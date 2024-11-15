from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserCadastro(AbstractUser):
    nome_mercado = models.CharField(max_length=110, blank=True, null=False)
    cnpj = models.CharField(max_length=15, blank=True, null=False)
    endereco = models.CharField(max_length=110, blank=True, null=False)
    telefone = models.CharField(max_length=15, blank=True, null=False)
    email = models.EmailField(blank=True, null=False, unique=True)

    groups = models.ManyToManyField(Group, related_name='usercadastro_groups') 
    user_permissions = models.ManyToManyField(Permission, related_name='usercadastro_permissions')

    USERNAME_FIELD = 'nome_mercado'

    def __str__(self):
        return self.nome_mercado
    
    

class Adicionar_oferta(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=600)
    categoria = models.CharField(max_length=100)
    preco_antigo = models.DecimalField(max_digits=10,  decimal_places=2)
    preco_atual = models.DecimalField(max_digits=10,  decimal_places=2)
    quantidade_disponivel = models.IntegerField()
    data_expiracao = models.DateField()
    imagem_produto = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome

class Oferta(Adicionar_oferta):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('expirado', 'Expirado'),
    ]

    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return self.nome
