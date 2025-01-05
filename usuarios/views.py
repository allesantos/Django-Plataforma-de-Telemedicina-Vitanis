from django.contrib.auth import login, authenticate # Funções de autenticação e login do Django
from django.contrib.auth.models import User # Modelo padrão de usuário do Django
from django.shortcuts import render, redirect  # Funções auxiliares para renderizar templates e redirecionar
from django.contrib.messages import constants # Constantes para categorizar mensagens
from django.contrib import messages # Sistema de mensagens do Django
from django.contrib import auth # Biblioteca de autenticação do Django

def cadastro(request):
    # Lida com o fluxo de cadastro de usuários
    if request.method == "GET":
        # Renderiza o template de cadastro ao acessar a página
        return render(request, 'cadastro.html')   
    elif request.method == "POST":
        # Captura os dados enviados pelo formulário
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')
        is_medico = request.POST.get('is_medico')  # Verifica se o checkbox "Você é médico?" foi marcado      
        # Verifica se o nome de usuário já existe
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Este usuário já existe!')
            return redirect('/usuarios/cadastro')
        # Verifica se as senhas são iguais
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha e o confirmar senha devem ser iguais!')
            return redirect('/usuarios/cadastro')
        # Verifica se a senha tem pelo menos 6 caracteres
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres.')
            return redirect('/usuarios/cadastro')      
        try:
            # Cria o usuário no banco de dados
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            # Autentica o usuário recém-criado
            user = authenticate(request, username=username, password=senha)
            # Realiza o login automático após cadastro
            login(request, user)
            # Redireciona para o fluxo de cadastro de médico, se marcado
            if is_medico == 'on':  # Checkbox marcado
                return redirect('/medicos/cadastro_medico')             
            # Redireciona para a página de login se não for médico
            return redirect('/usuarios/login')  
        except Exception as e:
            # Adiciona uma mensagem de erro em caso de falha no cadastro
            messages.add_message(request, constants.ERROR, f'Erro ao realizar o cadastro: {e}')
            return redirect('/usuarios/cadastro')
        
def login_view(request):
    # Lida com o fluxo de login
    if request.method == "GET":
        # Renderiza o template de login
        return render(request, 'login.html')
    elif request.method == "POST":
        # Captura os dados enviados pelo formulário de login
        username = request.POST.get('username')
        senha = request.POST.get("senha")
         # Tenta autenticar o usuário
        user = auth.authenticate(request, username=username, password=senha)
        if user:
            # Realiza o login se a autenticação for bem-sucedida
            auth.login(request, user)
            return redirect('/pacientes/home')
        # Adiciona uma mensagem de erro em caso de falha na autenticação
        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')

def sair(request):
    # Realiza o logout do usuário
    auth.logout(request)
    return redirect('/usuarios/login')