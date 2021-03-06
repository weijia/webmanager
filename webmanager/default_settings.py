INSTALLED_APPS += (
    'reversion',  # This is required in serializer_generator.py to support revision for model
    'provider',
    'provider.oauth2',
    'simplemenu',
    'webmanager',
    'bootstrapform',
    'userenabootstrap',
    'easy_thumbnails',
    'userena',
    # 'social_auth',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.contrib.auth.context_processors.auth',
)

AUTHENTICATION_BACKENDS += (
    'userena.backends.UserenaAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend'
)

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'webmanager.MyProfile'

USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

USERENA_ACTIVATION_REQUIRED = False
USERENA_SIGNIN_AFTER_SIGNUP = True
