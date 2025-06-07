from django.db import models

# Create your models here.
class produto(models.Model):
    cod_produto = models.Charfield(max.length=5)
    nome = models.Charfield(max.length=200)
    categoria = models.Charfield(max.length=50)
    estoque_atual = models.Charfield()
    estoque_minimo = models.Charfield()

    def __str__(self):
        return self.nome
