from django.db import models


class LadoEsquerdo(models.Model):
    background = models.CharField(max_length=7, default='#FFFFFF')
    estilo_letra_titulo = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_titulo = models.CharField(max_length=7, default='#000000')
    estilo_letra_texto = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_texto = models.CharField(max_length=7, default='#333333')
    logo = models.ImageField(upload_to='img_logo_index')

    def __str__(self):
        return f"LadoEsquerdo Config: {self.background}, {self.estilo_letra_titulo}, {self.cor_letra_titulo}, {self.estilo_letra_texto}, {self.cor_letra_texto}"


class LadoDireito(models.Model):
    background = models.CharField(max_length=7, default='#FFFFFF')
    estilo_letra_titulo = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_titulo = models.CharField(max_length=7, default='#333333')
    estilo_letra_texto = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_texto = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return f"LadoDireito Config: {self.background}, {self.estilo_letra_titulo}, {self.cor_letra_titulo}, {self.estilo_letra_texto}, {self.cor_letra_texto}"
