from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    site = models.TextField(max_length=255)
    data_pesquisa = models.DateField(auto_now=True)
    link_imagem = models.TextField(max_length=500, default='https://via.placeholder.com/150')

    
