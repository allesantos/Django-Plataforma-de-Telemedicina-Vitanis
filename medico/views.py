from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Especialidades, DadosMedico, is_medico, DatasAbertas
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime, timedelta
from paciente.models import Consulta, Documento

# Login de usuários, redireciona conforme o grupo
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("senha")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redireciona baseado no grupo do usuário
            if user.groups.filter(name="Medicos").exists():
                return redirect("/medicos/consultas_medico/")
            else:
                return redirect("/pacientes/home/") 
        else:
            return render(request, "login.html", {"error": "Usuário ou senha inválidos"})
    return render(request, "login.html")

# Cadastro de médicos, apenas se ainda não cadastrado
@login_required
def cadastro_medico(request):
    if is_medico(request.user): # Impede duplicação de cadastro
        messages.add_message(request, constants.WARNING, 'Você já está cadastrado como médico.')
        return redirect('/medicos/abrir_horario')    
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        return render(request, 'cadastro_medico.html', {'especialidades': especialidades, 'is_medico': is_medico(request.user)})
    elif request.method == "POST":
        # Obtém os dados enviados pelo formulário para criar o cadastro do médico
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        cim = request.FILES.get('cim') 
        rg = request.FILES.get('rg') 
        foto = request.FILES.get('foto') 
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')
        # Cria o objeto DadosMedico e salva no banco de dados
        dados_medico = DadosMedico(
            crm=crm,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            rg=rg,
            cedula_identidade_medica=cim,
            foto=foto,
            user=request.user,
            descricao=descricao,
            especialidade_id=especialidade,
            valor_consulta=valor_consulta
        )
        
        dados_medico.save()
        # Exibe mensagem de sucesso e redireciona o usuário
        messages.add_message(request, constants.SUCCESS, 'Cadastro médico realizado com sucesso.')
        return redirect('/medicos/abrir_horario')
    
# Abertura de horários de consulta para médicos   
@login_required
def abrir_horario(request):
    if not is_medico(request.user): # Apenas médicos podem acessar
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')
    if request.method == "GET":
        # Obtém dados do médico e horários abertos
        dados_medicos = DadosMedico.objects.get(user=request.user)
        datas_abertas = DatasAbertas.objects.filter(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_medicos': dados_medicos, 'datas_abertas': datas_abertas, 'is_medico': is_medico(request.user)})      
    elif request.method == "POST":
        # Cadastra um novo horário aberto para consultas
        data = request.POST.get('data')
        data_formatada = datetime.strptime(data, "%Y-%m-%dT%H:%M")
        # Valida se a data é válida
        if data_formatada <= datetime.now():
            messages.add_message(request, constants.WARNING, 'A data deve ser maior ou igual a data atual.')
            return redirect('/medicos/abrir_horario')      
        horario_abrir = DatasAbertas(
            data=data,
            user=request.user
        )
        horario_abrir.save()    
        # Exibe mensagem de sucesso
        messages.add_message(request, constants.SUCCESS, 'Horário cadastrado com sucesso.')
        return redirect('/medicos/abrir_horario')

# Lista consultas do médico logado
@login_required   
def consultas_medico(request):
    # Apenas médicos podem visualizar suas consultas
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')    
    # Busca o médico associado ao usuário logado, se existir
    medico_logado = None
    if hasattr(request.user, 'dadosmedico'):  # Verifica se o usuário possui DadosMedico
        medico_logado = request.user.dadosmedico  # Acessa o médico relacionado  
    dados_medicos = DadosMedico.objects.get(user=request.user)
    # Determina o prefixo com base no sexo
    if dados_medicos.sexo == 'M':
        prefixo = "Dr."
    elif dados_medicos.sexo == 'F':
        prefixo = "Dra."
    else:
        prefixo = "Dr(a)."

    hoje = datetime.now().date()
    # Obtém as consultas de hoje e as futuras
    consultas_hoje = Consulta.objects.filter(data_aberta__user=request.user).filter(data_aberta__data__gte=hoje).filter(data_aberta__data__lt=hoje + timedelta(days=1))
    consultas_restantes = Consulta.objects.exclude(id__in=consultas_hoje.values('id')).filter(data_aberta__user=request.user)
    return render(request, 'consultas_medico.html', {'dados_medicos': dados_medicos,'consultas_hoje': consultas_hoje, 'consultas_restantes': consultas_restantes, 'is_medico': is_medico(request.user), 'medico_logado': medico_logado,'prefixo': prefixo,})

# Exibe detalhes de uma consulta específica
@login_required
def consulta_area_medico(request, id_consulta):
    # Apenas médicos podem acessar os detalhes de uma consulta
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')    
    if request.method == "GET":
         # Obtém informações da consulta e documentos relacionados
        consulta = Consulta.objects.get(id=id_consulta)
        documentos = Documento.objects.filter(consulta=consulta)
        return render(request, 'consulta_area_medico.html', {'consulta': consulta, 'documentos': documentos,'is_medico': is_medico(request.user)}) 
    elif request.method == "POST":
        # Inicia a consulta e salva o link da chamada
        consulta = Consulta.objects.get(id=id_consulta)
        link = request.POST.get('link')
        # Verifica o status da consulta antes de iniciar
        if consulta.status == 'C': # Cancelada
            messages.add_message(request, constants.WARNING, 'Essa consulta já foi cancelada, você não pode inicia-la!')
            return redirect(f'/medicos/consulta_area_medico/{id_consulta}')
        elif consulta.status == "F": # Finalizada
            messages.add_message(request, constants.WARNING, 'Essa consulta já foi finalizada, você não pode inicia-la!')
            return redirect(f'/medicos/consulta_area_medico/{id_consulta}')    
        consulta.link = link
        consulta.status = 'I' # Iniciada
        consulta.save()
        messages.add_message(request, constants.SUCCESS, 'Consulta inicializada com sucesso.')
        return redirect(f'/medicos/consulta_area_medico/{id_consulta}')

# Finaliza uma consulta específica
@login_required
def finalizar_consulta(request, id_consulta):
    # Apenas médicos podem finalizar consultas
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')   
    consulta = Consulta.objects.get(id=id_consulta)
     # Verifica se o médico atual é o dono da consulta
    if request.user != consulta.data_aberta.user:
        messages.add_message(request, constants.ERROR, 'Essa consulta não é sua!')
        return redirect(f'/medicos/consulta_area_medico/{id_consulta}')
    consulta.status = 'F' # Finalizada
    consulta.save()
    return redirect(f'/medicos/consulta_area_medico/{id_consulta}')

# Adiciona documentos a uma consulta
def add_documento(request, id_consulta):
    # Apenas médicos podem adicionar documentos às consultas
    if not is_medico(request.user):
        messages.add_message(request, constants.WARNING, 'Somente médicos podem acessar essa página.')
        return redirect('/usuarios/sair')
    consulta = Consulta.objects.get(id=id_consulta)  
    # Verifica se o médico atual é o responsável pela consulta
    if consulta.data_aberta.user != request.user:
        messages.add_message(request, constants.ERROR, 'Essa consulta não é sua!')
        return redirect(f'/medicos/abrir_horario/')     
    titulo = request.POST.get('titulo')
    documento = request.FILES.get('documento')
    # Valida se um arquivo foi enviado
    if not documento:
        messages.add_message(request, constants.WARNING, 'Adicione o documento.')
        return redirect(f'/medicos/consulta_area_medico/{id_consulta}')
    documento = Documento(
        consulta=consulta,
        titulo=titulo,
        documento=documento
    )
    documento.save()
    messages.add_message(request, constants.SUCCESS, 'Documento enviado com sucesso!')
    return redirect(f'/medicos/consulta_area_medico/{id_consulta}')



