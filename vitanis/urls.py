from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static # Permite servir arquivos estáticos em ambiente de desenvolvimento
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Inclui as rotas definidas no aplicativo 'usuarios'
    path('medicos/', include('medico.urls')),   # Inclui as rotas definidas no aplicativo 'medico'
    path('pacientes/', include('paciente.urls')), # Inclui as rotas definidas no aplicativo 'paciente'
    path('', lambda request: redirect('/usuarios/login/')), # Redireciona a rota principal ('/') para a página de login de usuários
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Configura o servidor para servir arquivos de mídia (em desenvolvimento)
