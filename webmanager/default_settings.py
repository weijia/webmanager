INSTALLED_APPS += (
    'simplemenu',
    'webmanager',
    'bootstrapform',
    'userenabootstrap',
    'userena',
    'provider.oauth2',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
)

AUTHENTICATION_BACKENDS += ('django.contrib.auth.backends.ModelBackend',
                            'guardian.backends.ObjectPermissionBackend')

ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'webmanager.MyProfile'

USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

USERENA_ACTIVATION_REQUIRED = False
USERENA_SIGNIN_AFTER_SIGNUP = True
