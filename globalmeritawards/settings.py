
"""
Django settings for allifapperp project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os

from pathlib import Path
#from dotenv import load_dotenv

# Load environment variables from .env file
#load_dotenv()
#allif_get_env_var= os.environ.get

#BASE_DIR = Path(__file__).parent.parent.parent 

#load_dotenv(BASE_DIR / "../.env") #here you indicate where your .env file is
#env_path = load_dotenv(os.path.join(BASE_DIR, './vvvdd/.env'))
#load_dotenv(env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-c8*_cv^aw$^%(*k5zfx1+(svx3yw!448%^=ci6auje3ucz7gvn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Add a setting for maintenance mode

#if DEBUG:
    #STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#else:
    #STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#DEBUG = os.environ.get('ALLIF_DJANGO_DEBUG', '')
ALLOWED_HOSTS = ['ahmeddove.pythonanywhere.com','127.0.0.1','localhost','http://0.0.0.0:8000/']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$@($ofh@)3j5cly(5yo-b6+3r)7pg7flt&m-z+*kon)2)%q*#0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['globalmeritawards.pythonanywhere.com','127.0.0.1','localhost','http://0.0.0.0:8000/']

#SECRET_KEY =allif_get_env_var("ALLIF_DJANGO_SECRET_KEY")
#EMAIL_BACKEND=allif_get_env_var("ALLIF_EMAIL_BACKEND","email-backend")
#EMAIL_HOST=allif_get_env_var('ALLIF_EMAIL_HOST','email-host')
#EMAIL_PORT=allif_get_env_var('ALLIF_EMAIL_PORT','email-port')
#EMAIL_USE_TLS=allif_get_env_var('ALLIF_EMAIL_USE_TLS','email-use-tls')
#EMAIL_HOST_USER=allif_get_env_var('ALLIF_EMAIL_HOST_USER','email-host-user')
#EMAIL_HOST_PASSWORD=allif_get_env_var('ALLIF_EMAIL_HOST_PASSWORD','email-host-password')


############### uncomment below for production ################
#SECURE_HSTS_SECONDS = 31536000
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_SSL_REDIRECT = True# Set this to true in production
#SESSION_COOKIE_SECURE = True
#SECURE_HSTS_PRELOAD = True
#CSRF_COOKIE_SECURE = True


# Application definition
#EMAIL_HOST = os.getenv("EMAIL_HOST")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    "django.contrib.humanize",
    'crispy_forms',
    'import_export',
    
    
     'awards',
     'loginapp',
     
     
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

ROOT_URLCONF = 'globalmeritawards.urls'

# below is for auto logout when there is inactivity... there is two ways to do it as below.
#AUTO_LOGOUT = {'IDLE_TIME': 60}  # logout after 10 minutes of downtime
from datetime import timedelta
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=60),
    'loginapp:userLoginPage': True,
}

# django_project/settings.py
LOGIN_REDIRECT_URL="home"
LOGOUT_REDIRECT_URL="home"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'allifmaalcommonapp.preprocessor.allifmaalcommonappglobalVariables',
                #'allifmaalcommonapp.preprocessor.allifUserSessions',
            ],
        },
    },
]

WSGI_APPLICATION = 'globalmeritawards.wsgi.application'
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get('DB_USER'),
        "PASSWORD": os.environ.get('DB_USER_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('DB_PORT'),
    }
}
"""
""""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'allifmaal_db',
        'USER': 'root',
        'PASSWORD': 'amd30974153',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}  
"""

"""... below worked for me as of 22nd feb 2024
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MYSQL',
        'USER': 'root',
        'PASSWORD': 'hidden',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}  

"""


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# comments
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#PATH WHERE UPLOADED FILES WILL BE STORED...in the media folder
MEDIA_ROOT=os.path.join(BASE_DIR,'static/media')
MEDIA_URL='/media/'#fetch images/media using this path when viewing through the browser...this folder will be created automatically when we upload the first image
AUTH_USER_MODEL = 'loginapp.User'
#SENDSMS_BACKEND = 'allifmaalusersapp.mysmsbackend.SmsBackend'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Mogadishu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT='static'
#STATICFILES_LOCATION='static'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_LOCATION='static'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

MEDIA_ROOT=os.path.join(BASE_DIR,'static/media')
#PATH WHERE UPLOADED FILES WILL BE STORED...in the media folder
MEDIA_URL='/media/'#fetch images/media using this path when viewing through the browser...this folder will be created automatically when we upload the first image


AUTH_USER_MODEL = 'loginapp.User'
#SENDSMS_BACKEND = 'allifmaalusersapp.mysmsbackend.SmsBackend'





