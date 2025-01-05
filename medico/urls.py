from django.urls import path
from . import views

# Define as rotas para a aplicação
urlpatterns = [
    path("login/", views.login_view, name="login"), # Rota para a página de login
    path('cadastro_medico/', views.cadastro_medico, name="cadastro_medico"), # Rota para o cadastro de médicos
    path('abrir_horario/', views.abrir_horario, name="abrir_horario"), # Rota para abrir horários disponíveis
    path('consultas_medico/', views.consultas_medico, name="consultas_medico"), # Rota para listar as consultas do médico
    path('consulta_area_medico/<int:id_consulta>/', views.consulta_area_medico, name="consulta_area_medico"), # Rota para acessar os detalhes de uma consulta
    path('finalizar_consulta/<int:id_consulta>/', views.finalizar_consulta, name="finalizar_consulta"), # Rota para finalizar uma consulta  
    path('add_documento/<int:id_consulta>/', views.add_documento, name="add_documento"),  # Rota para adicionar documentos a uma consulta
]