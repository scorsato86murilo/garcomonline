from django.contrib import admin
from .models import LadoEsquerdo, LadoDireito, NomeEstabelecimento, TamanhoImg, TituloPagina, Avisos

admin.site.register(LadoEsquerdo)
admin.site.register(LadoDireito)
admin.site.register(NomeEstabelecimento)
admin.site.register(TamanhoImg)
admin.site.register(TituloPagina)
admin.site.register(Avisos)
