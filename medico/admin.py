from django.contrib import admin
from .models import Especialidades, DadosMedico, DatasAbertas

# Registro de modelos no painel de administração
admin.site.register(Especialidades) # Modelo para gerenciar especialidades médicas
admin.site.register(DadosMedico) # Modelo para gerenciar dados dos médicos
admin.site.register(DatasAbertas) # Modelo para gerenciar datas disponíveis para consultas
