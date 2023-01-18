# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!^effq!a22_h@k62f7)i$p)y=$t090^$wib&q@32pzn+i&7a2m'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_and_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Football1!'
    }
}