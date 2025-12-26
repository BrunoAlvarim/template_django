from django.db import models
from uuid import uuid4
from datetime import datetime

class Funcionario(models.Model):

    EMPRESA = (
        ('M','Matriz')
        ('A','Filial Argentina')
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
            #choices funciona para travar as escolhas do usuario ao que preencher nesse campo, travando nas opções que eu travei na dupla acima
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
    create_at = models.DateField(
        null=False,
        blank=False,
        default=datetime,
        editable=False
    )
    update_at = models.DateField(
        null=True
    )
    def __str__(self):
        return self.nome