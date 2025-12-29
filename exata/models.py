from django.db import models
from uuid import uuid4
from datetime import datetime

class Funcionario(models.Model):
    EMPRESA = (
        ('M','Matriz'),
        ('A','Filial Argentina'),
        ('E','Filial Estados Unidos')
    )
    nome = models.CharField(
        max_length=200,
        null=False,
        blank=False 
    )
    funcao = models.CharField(
        max_length=200,
        null=False,
        blank=False 
    )
    empresa = models.CharField(
            max_length=1,
            blank=False,
            null=False,
            choices=EMPRESA,
            default='M'
    )
    flag_ativo = models.BooleanField(
        null=False,
        blank=False,
        default=1
    )
    hash_id = models.UUIDField(
        null=False,
        blank=False,
        default=uuid4,
        editable=False, 
        unique=True
    )
    # auto_now_add: grava a data quando cria
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    
    # auto_now: atualiza a data toda vez que o objeto mudar
    update_at = models.DateTimeField(
        auto_now=True,
        null=True
    )
        
    # serve para representar o objeto externamente, caso seja chamado em algum metodo sera 
    # retornado o nome e nao o id ou a chave
    def __str__(self): 
        return self.nome