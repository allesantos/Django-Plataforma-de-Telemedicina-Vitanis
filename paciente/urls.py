from django.urls import path
from . import views

# Definição das rotas (URLs) para as views
urlpatterns = [
    path('home/', views.home, name="home"), # Rota principal da home
    path('escolher_horario/<int:id_dados_medicos>/', views.escolher_horario, name="escolher_horario"), # Rota para escolher horário
    path('agendar_horario/<int:id_data_aberta>/', views.agendar_horario, name="agendar_horario"),  # Rota para agendar horário
    path('minhas_consultas/', views.minhas_consultas, name="minhas_consultas"), # Rota para visualizar as consultas do usuário
    path('consulta/<int:id_consulta>/', views.consulta, name="consulta"), # Rota para detalhes da consulta
    path('cancelar_consulta/<int:id_consulta>/', views.cancelar_consulta, name="cancelar_consulta"), # Rota para cancelar consulta
]