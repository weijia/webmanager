INSTALLED_APPS += (
    'simplemenu',
    'webmanager',
    'bootstrapform',
    'userenabootstrap',
    'userena',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
)


ANONYMOUS_USER_ID = -1


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'webmanager.MyProfile'

USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/userena/signin/'
LOGOUT_URL = '/userena/signout/'

#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

USERENA_ACTIVATION_REQUIRED = False
USERENA_SIGNIN_AFTER_SIGNUP = True
