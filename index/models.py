from django.db import models


class NomeEstabelecimento(models.Model):
    nome = models.CharField(max_length=100, default='Nome Do Mercado')

    def __str__(self):
        return self.nome


class LadoEsquerdo(models.Model):
    background = models.CharField(max_length=7, default='#FFFFFF')
    texto = models.TextField(default="Texto do lado esquerdo")
    estilo_letra_titulo = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_titulo = models.CharField(max_length=7, default='#000000')
    estilo_letra_texto = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_texto = models.CharField(max_length=7, default='#333333')
    logo = models.ImageField(upload_to='img_logo_index')

    def __str__(self):
        return f"LadoEsquerdo Config: {self.background}, {self.estilo_letra_titulo}" f"Cor do nome da empresa: {self.cor_letra_titulo}, {self.estilo_letra_texto}, {self.cor_letra_texto}"


class LadoDireito(models.Model):
    background = models.CharField(max_length=7, default='#FFFFFF')
    titulo = models.CharField(max_length=100, default='Bem Vindo!')
    texto = models.TextField(default='Texto do lado direito')
    estilo_letra_titulo = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_titulo = models.CharField(max_length=7, default='#333333')
    estilo_letra_texto = models.CharField(max_length=100, default='Arial, sans-serif')
    cor_letra_texto = models.CharField(max_length=7, default='#000000')


    def __str__(self):
        return f"LadoDireito Config: {self.background}, {self.estilo_letra_titulo}, {self.cor_letra_titulo}, {self.estilo_letra_texto}, {self.cor_letra_texto}"


class TamanhoImg(models.Model):
    altura = models.IntegerField(default=0)  # Altura da imagem, valor padrão 40
    largura = models.IntegerField(default=40)  # Largura da imagem, valor padrão 40


    def __str__(self):
        return f"Altura: {self.altura}, Largura: {self.largura}"


class TituloPagina(models.Model):
    titulo = models.CharField(max_length=70, default='Bem Vindo!')
