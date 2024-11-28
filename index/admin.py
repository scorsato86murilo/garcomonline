from django.contrib import admin
from .models import LadoEsquerdo, LadoDireito, NomeEstabelecimento, TamanhoImg

admin.site.register(LadoEsquerdo)
admin.site.register(LadoDireito)
admin.site.register(NomeEstabelecimento)
admin.site.register(TamanhoImg)
