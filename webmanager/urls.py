from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^cmd/$', 'webmanager.views.cmd'),
    url(r'^django_version/$', 'webmanager.views.version'),
    url(r'^create_admin_user/$', 'webmanager.views.handle_create_admin_req'),
    url(r'^login_and_go_home/$', 'webmanager.views.login_and_go_home'),
)

try:
    from provider.oauth2.backends import AccessTokenBackend

    urlpatterns += patterns('',
        url(r'^login_from_oauth2/$', 'webmanager.views_oauth2.login_from_oauth2'),
    )
except ImportError:
    pass

# The following can be used to do mail backend testing
try:
    import backends.mail_backend
    urlpatterns.extend([url(r'^test_email/$', 'backends.mail_backend.mail_backend_test')])
except ImportError:
    pass