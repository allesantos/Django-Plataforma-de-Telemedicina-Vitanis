from django.contrib import admin
from .models import Consulta, Documento

# Registrando os modelos Consulta e Documento no admin do Django
admin.site.register(Consulta) # Registrar o modelo Consulta
admin.site.register(Documento) # Registrar o modelo Documento