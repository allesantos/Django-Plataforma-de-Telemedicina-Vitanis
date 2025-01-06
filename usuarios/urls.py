from django.urls import path
from . import views

urlpatterns = [

    # Rota para a página de cadastro de usuários
    path('cadastro/', views.cadastro, name="cadastro"),

    # Rota personalizada para login de usuários
    path('login/', views.login_view, name="login"),

    # Rota para logout (sair da sessão do usuário)
    path('sair/', views.sair, name="sair")
]