# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mjs9%^#kucp!4sl6v#+97f$n4h_r4d42i*k=dp8x(xog^t(s#i'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wifes_portfolio_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
