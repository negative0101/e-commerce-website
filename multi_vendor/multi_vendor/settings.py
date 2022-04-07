import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-nz!c_oe3n7c^cm@7s%7tt8qd*p3$4l0aixdop2i#woicqww710'

DEBUG = True
ALLOWED_HOSTS = ['localhost','127.0.0.1','bigblackcat.herokuapp.com']

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
    'whitenoise.middleware.WhiteNoiseMiddleware',

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

DEFAULT_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'd7obasm4lvmjsu',
    'USER': 'hprartgirtsxjj',
    'PASSWORD': 'b41f073d2eec16a24e5903871021d5df4f1a83b362aed8aa244d026d669e306c',
    'HOST': 'ec2-34-247-72-29.eu-west-1.compute.amazonaws.com',
    'PORT': '5432',
}
DATABASES = {
    'default': DEFAULT_DATABASE_CONFIG

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

BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR2, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR2, 'static'),)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_PUB_KEY = 'pk_test_51Kf72LBEIIlaEJA21ViEDY0oqQt0FTc5sL1qqmgMQ6h77TTSeBQdkdkh2LaWgEXBhqf4nA498oEsTFqIopcZLnsJ0052OCxxak'
STRIPE_SECRET_KEY = 'sk_test_51Kf72LBEIIlaEJA2UXSdV3iVkA9BtVOBEsep7191uGTEwDSK7458AhSiTlLd4xlSyRBe3qXDwPiCtaxqUKCOzHaf00TPZFDmCf'
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

cloudinary.config(
    cloud_name="hddpogror",
    api_key="531884663832477",
    api_secret="brcPmmfeEjjrPxtccjgV6CkVm4U",

)
