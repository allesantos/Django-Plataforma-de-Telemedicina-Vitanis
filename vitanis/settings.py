
from pathlib import Path
import os
from django.contrib.messages import constants

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta para segurança da aplicação
SECRET_KEY = 'django-insecure-=2yt8o0qayd_@xp5^gu^(agh7ye@=q_^f04^rj*3#jnqp+yxv7'

# Define o modo de depuração 
DEBUG = True

# Lista de hosts permitidos para acessar o projeto
ALLOWED_HOSTS = []

# Aplicativos instalados (apps nativos e criados)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios', # App de usuários
    'medico',   # App para médicos
    'paciente'  # App para pacientes
]

# Middlewares para processamento de requisições e segurança
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração das URLs principais
ROOT_URLCONF = 'vitanis.urls'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Diretório de templates
        'APP_DIRS': True, # Busca templates dentro de cada app
        'OPTIONS': {
            'context_processors': [ # Processadores de contexto
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração para o servidor WSGI
WSGI_APPLICATION = 'vitanis.wsgi.application'

# Configuração do banco de dados (SQLite por padrão)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validações de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de idioma e fuso horário
LANGUAGE_CODE = 'pt-BR' # Idioma padrão
TIME_ZONE = 'America/Sao_Paulo' # Fuso horário local

# Internacionalização e localização
USE_I18N = True
USE_TZ = False # Desativado para evitar problemas com datetime

# Configurações de arquivos estáticos e mídia
STATIC_URL = '/static/' # URL para arquivos estáticos
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),) # Diretórios estáticos
STATIC_ROOT = os.path.join('static') # Diretório para coleta de arquivos estáticos
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Diretório para uploads
MEDIA_URL = '/media/' # URL para arquivos de mídia

# Configuração de ID automático padrão para modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração de categorias de mensagens
MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}

# Configuração de logging (registros de eventos)
LOGGING = {
    'version': 1, # Versão do formato de logging
    'disable_existing_loggers': False, # Mantém loggers padrão ativos
    'formatters': { # Formatos de mensagens de log
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': { # Configurações de saída de logs
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': { # Loggers específicos
        'django': {
            'handlers': ['console'],
            'level': 'INFO', # Logs do Django
        },
        'paciente': {  
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False, # Logs específicos do app 'paciente'
        },
    },
}
