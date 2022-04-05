from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-nz!c_oe3n7c^cm@7s%7tt8qd*p3$4l0aixdop2i#woicqww710'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multi_vendor.core',
    'multi_vendor.vendor',
    'multi_vendor.product',
    'multi_vendor.cart',
    'multi_vendor.order',
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

ROOT_URLCONF = 'multi_vendor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'multi_vendor.product.context_processor.menu_categories',
                'multi_vendor.cart.context_processor.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'multi_vendor.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)







DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_PUB_KEY = 'pk_test_51Kf72LBEIIlaEJA21ViEDY0oqQt0FTc5sL1qqmgMQ6h77TTSeBQdkdkh2LaWgEXBhqf4nA498oEsTFqIopcZLnsJ0052OCxxak'
STRIPE_SECRET_KEY = 'sk_test_51Kf72LBEIIlaEJA2UXSdV3iVkA9BtVOBEsep7191uGTEwDSK7458AhSiTlLd4xlSyRBe3qXDwPiCtaxqUKCOzHaf00TPZFDmCf'
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
