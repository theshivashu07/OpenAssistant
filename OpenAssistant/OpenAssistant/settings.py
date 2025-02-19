"""
Django settings for OpenAssistant project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q-7wqv3=-(^9tu6%*trzw!*qwdwlnhiug)j1zh^mj(ija77=!#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# ADD - these below lines are only for set another address+port for our website
from django.core.management.commands.runserver import Command as runserver        # adding  
runserver.default_port = '8080'        # <-- Your port                                                                      # adding  
runserver.default_port = '1234'        # <-- Your port                                                                       # adding  
# runserver.default_addr = '127.0.0.1'                                                                                               # adding  
runserver.default_addr = 'localhost'                                                                                                  # adding  



# 404 default
# HANDLER404 = 'django.views.generic.TemplateView.as_view(template_name="404.html")'
# HANDLER404 = 'django.views.generic.TemplateView.as_view(template_name="theLearnings/Client/404.html")' 
# HANDLER404 = 'theLearnings.views.your_404_view' 
handler404 = 'theLearnings.views.handler404'  



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'ckeditor',
    'ckeditor_uploader',

    'Admin',     # adding  
    'Client',     # adding  
    'Home',     # adding  
    'API',     # adding  
    'theArticals',
    'theProblems',
    'theLearnings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OpenAssistant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"_templates"],    # 'DIRS': [],
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'OpenAssistant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Dont use below line, because if we using this then automatically our time is now showing well, and save less 05:30 hours of actual timing...
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
TIME_ZONE =  'Asia/Kolkata'     # adding  
USE_I18N = True                          # adding  


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# STATIC_URL = 'static/'     # hiding  
STATIC_URL = '_static/'     # adding  

# Addituinal Adding, So that static files are accessable, 
STATICFILES_DIRS = [          # adding  
    BASE_DIR,"_static"          # adding  
    # BASE_DIR/"_static"      # adding  
]                                                    # adding  


# Because of uploading media files, follow below!! 
# MEDIA_ROOT =  os.path.join(BASE_DIR, '_uploads') 
MEDIA_ROOT =  BASE_DIR / '_uploads'       # adding  
MEDIA_URL = '/_uploads/'                               # adding  



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# below things is for MESSAGE
from django.contrib.messages import constants as messages        # adding  
MESSAGE_TAGS = {                                                                                      # adding  
    messages.ERROR : 'danger',                                                                    # adding  
}                                                                                                                           # adding  




CKEDITOR_BASEPATH = "/_static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "/_static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]),
    },
}










