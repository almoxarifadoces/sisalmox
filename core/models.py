from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
   
        
class Material(models.Model):
    codigo = models.CharField('Código SICON', max_length=7)
    name = models.CharField('Nome', max_length=100)
    description = models.CharField('Descrição', blank=True, max_length=100)
    unid = models.CharField('Unidades', max_length=100)
    available = models.BooleanField('Disponível', default=True)    

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
