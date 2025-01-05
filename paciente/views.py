from django.shortcuts import render, redirect
from medico.models import DadosMedico, Especialidades, DatasAbertas, is_medico
from datetime import datetime, timedelta
from .models import Consulta, Documento
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required

# Página principal com filtros e listagem de médicos
@login_required
def home(request):
    # Inicializa as variáveis
    medico_logado = None
    prefixo_medico_logado = None
    usuario_logado = None
    # Verifica se o usuário logado é um médico
    if hasattr(request.user, 'dadosmedico'):  # Verifica se o usuário possui DadosMedico
        medico_logado = request.user.dadosmedico  # Acessa o médico relacionado
      # Determina o prefixo com base no gênero
        if medico_logado.sexo == 'M': 
            prefixo_medico_logado = "Dr."
        elif medico_logado.sexo == 'F':
            prefixo_medico_logado = "Dra."
        else:
            prefixo_medico_logado = "Dr(a)."
    else:
        # Caso seja um paciente, define o "username"
        usuario_logado = request.user.username    
    # Filtros para a listagem de médicos
    if request.method == "GET":
        medico_filtrar = request.GET.get('medico')
        especialidades_filtrar = request.GET.getlist('especialidades')
        medicos = DadosMedico.objects.all()
    if medico_filtrar:
        medicos = medicos.filter(nome__icontains = medico_filtrar)
    if especialidades_filtrar:
        medicos = medicos.filter(especialidade_id__in=especialidades_filtrar)
    # Adiciona o prefixo a cada médico
    medicos_enriquecidos = []
    for medico in medicos:
        if medico.sexo == 'M':
            prefixo = "Dr."
        elif medico.sexo == 'F':
            prefixo = "Dra."
        else:
            prefixo = "Dr(a)."
        medicos_enriquecidos.append({'medico': medico, 'prefixo': prefixo})   
    especialidades = Especialidades.objects.all() 
    return render(
        request,
        'home.html',
        {
            'medicos': medicos_enriquecidos,  # Lista enriquecida com prefixos
            'especialidades': especialidades,
            'is_medico': is_medico(request.user),
            'medico_logado': medico_logado,
            'prefixo_medico_logado': prefixo_medico_logado,  # Prefixo do médico logado
            'usuario_logado': usuario_logado,  # Nome do paciente, caso seja paciente
        },
    )

# Página para escolher horário de consulta
@login_required
def escolher_horario(request, id_dados_medicos):
    if request.method == "GET":
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = DatasAbertas.objects.filter(user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)
        # Determinar o prefixo com base no sexo do médico
        if medico.sexo == 'M':  # Substitua 'sexo' pelo nome correto do campo
            prefixo = "Dr."
        elif medico.sexo == 'F':
            prefixo = "Dra."
        else:
            prefixo = "Dr(a)."
        return render(request, 'escolher_horario.html', {'medico': medico, 'datas_abertas': datas_abertas, 'is_medico': is_medico(request.user), 'prefixo': prefixo, })

# Função para agendar horário de consulta
@login_required
def agendar_horario(request, id_data_aberta):
    if request.method == "GET":
        data_aberta = DatasAbertas.objects.get(id=id_data_aberta)

        horario_agendado = Consulta(
            paciente=request.user,
            data_aberta=data_aberta
        )
        horario_agendado.save()
        data_aberta.agendado = True
        data_aberta.save()
        messages.add_message(request, constants.SUCCESS, 'Horário agendado com sucesso.')
        return redirect('/pacientes/minhas_consultas/')
    
# Página para visualizar e filtrar consultas do paciente
@login_required   
def minhas_consultas(request):
    data = request.GET.get('data')
    especialidade = request.GET.get('especialidade')
     # Inicializa as consultas do paciente com data futura
    minhas_consultas = Consulta.objects.filter(
        paciente=request.user,
        data_aberta__data__gte=datetime.now()  # Corrige o acesso ao campo 'data' do modelo relacionado
    )
     # Filtro por data
    if data:
        try:
            # Converte o valor recebido para uma data válida
            data_especifica = datetime.strptime(data, "%Y-%m-%d")
            proximo_dia = data_especifica + timedelta(days=1)

            # Filtra pelo intervalo do dia
            minhas_consultas = minhas_consultas.filter(
                data_aberta__data__gte=data_especifica,
                data_aberta__data__lt=proximo_dia
            )
        except ValueError:
            # Log ou ação em caso de data inválida
            print(f"Erro: Data inválida fornecida: {data}")
      # Filtro por especialidade
    if especialidade:
        minhas_consultas = minhas_consultas.filter(data_aberta__user__dadosmedico__especialidade__id=especialidade)
    # Determina o prefixo para cada médico
    for consulta in minhas_consultas:
        medico = consulta.data_aberta.user.dadosmedico
        if medico.sexo == 'M':
            consulta.medico_prefixo = "Dr."
        elif medico.sexo == 'F':
            consulta.medico_prefixo = "Dra."
        else:
            consulta.medico_prefixo = "Dr(a)."  
    especialidades = Especialidades.objects.all()
    return render(
        request, 
        'minhas_consultas.html', 
        {
            'minhas_consultas': minhas_consultas, 
            'especialidades': especialidades, 
            'is_medico': is_medico(request.user)
        }
    )

# Detalhes da consulta
@login_required    
def consulta(request, id_consulta):
    if request.method == 'GET':
        consulta = Consulta.objects.get(id=id_consulta)
        dado_medico = DadosMedico.objects.get(user=consulta.data_aberta.user)
        documentos = Documento.objects.filter(consulta=consulta)       
         # Determina o prefixo com base no sexo
        if dado_medico.sexo == 'M':
            prefixo = "Dr."
        elif dado_medico.sexo == 'F':
            prefixo = "Dra."
        else:
            prefixo = "Dr(a)."     
        return render(request, 'consulta.html', {'consulta': consulta, 'dado_medico': dado_medico, 'documentos':documentos, 'prefixo': prefixo, 'is_medico': is_medico(request.user)})

# Função para cancelar consulta
@login_required   
def cancelar_consulta(request, id_consulta):
    consulta = Consulta.objects.get(id=id_consulta)
    if request.user != consulta.paciente:
        messages.add_message(request, constants.ERROR, 'Esta consulta não é sua!')
        return redirect(f'/pacientes/home/')   
    consulta.status = 'C'
    consulta.save()
    return redirect(f'/pacientes/consulta/{id_consulta}') 