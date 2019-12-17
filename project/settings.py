import os

#Basic settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY',' ')
DEBUG = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'pwa',
    'pages',
    'api',
    'mobile',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database and Auth settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ' ',
        'USER': ' ',
        'PASSWORD': '',
        'HOST': ' ',
    }
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

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

#Django allauth settings
ACCOUNT_EMAIL_VERIFICATION = "Optional"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 12
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 7200
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
AUTH_USER_MODEL='api.CustomUser'
LOGIN_REDIRECT_URL= "/mobile/mobile"

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

#Rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
}

#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', ' ')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ' '


#Stripe settings for payment
STRIPE_SECRET_KEY = ' '
STRIPE_PUBLISHABLE_KEY = ' '

#Django pwa settings so site can be installed as an app
PWA_APP_NAME = ' '
PWA_APP_DESCRIPTION = " "
PWA_APP_THEME_COLOR = ' '
PWA_APP_BACKGROUND_COLOR = ' '
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/mobile/mobile'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icons/favicon.ico',
        'sizes': '180x180'
    },
    {
        'src': '/static/images/icons/icon-72x72.png',
        'sizes': '72x72'
    },
    {
        'src': '/static/images/icons/icon-96x96.png',
        'sizes': '96x96'
    },
    {
        'src': '/static/images/icons/icon-128x128.png',
        'sizes': '128x128'
    },
    {
        'src': '/static/images/icons/icon-144x144.png',
        'sizes': '144x144'
    },
    {
        'src': '/static/images/icons/icon-192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/icons/icon-384x384.png',
        'sizes': '384x384'
    },
    {
        'src': '/static/images/icons/icon-512x512.png',
        'sizes': '512x512'
    }
]

PWA_APP_SPLASH_SCREEN = [
{
'src': '/static/images/icons/splash-640x1136.png',
'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-750x1334.png',
'media': '(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-1242x2208.png',
'media': '(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-750x1624.png',
'media': '(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-828x1792.png',
'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-1536x2048.png',
'media': '(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-1668x2224.png',
'media': '(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-1668x2388.png',
'media': '(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)'
},
{
'src': '/static/images/icons/splash-2048x12732.png',
'media': '(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)'
}
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
SITE_ID=
