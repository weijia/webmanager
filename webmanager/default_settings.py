INSTALLED_APPS += (
    'simplemenu',
    'webmanager',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
)

AUTHENTICATION_BACKENDS += ('django.contrib.auth.backends.ModelBackend',
                            'guardian.backends.ObjectPermissionBackend')

ANONYMOUS_USER_ID = -1


