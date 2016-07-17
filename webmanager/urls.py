from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from djangoautoconf.auto_conf_urls import add_to_root_url_pattern, exc_wrapper_for_url_pattern


urlpatterns = patterns('',
                       url(r'^cmd/$', 'webmanager.views.cmd'),
                       url(r'^django_version', 'webmanager.views.version'),
                       url(r'^create_admin_user', 'webmanager.views.handle_create_admin_req'),
                       url(r'^login_and_go_home', 'webmanager.views.login_and_go_home'),
                       url(r'^test_login', 'webmanager.views.test_login'),
                       url(r'^raise_error', 'webmanager.views.raise_error'),
                       url(r'^access_token/$', 'webmanager.views.handle_get_access_token_req'),
)

#
# # @ignore_exc_with_result([], ImportError)
# @exc_wrapper_for_url_pattern
# def get_access_token_backend_patterns():
#     from provider.oauth2.backends import AccessTokenBackend
#
#     return [
#         url(r'^login_from_oauth2/$', 'webmanager.views_oauth2.login_from_oauth2'),
#         url(r'^access_token/$', 'webmanager.views.handle_get_access_token_req'),
#         url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
#     ]
#
#
# @exc_wrapper_for_url_pattern
# def get_captcha_patterns():
#     from captcha.fields import CaptchaField
#
#     return [
#         url(r'^captcha/$', 'webmanager.views_captcha.some_view'),
#         url(r'^captcha/', include('captcha.urls')),
#     ]
#
#
# @exc_wrapper_for_url_pattern
# def get_test_mail_patterns():
#     import backends.mail_backend
#
#     return [url(r'^test_email/$', 'backends.mail_backend.mail_backend_test')]
#
#
# urlpatterns.extend(get_captcha_patterns())
# urlpatterns.extend(get_access_token_backend_patterns())
# # The following can be used to do mail backend testing
# urlpatterns.extend(get_test_mail_patterns())
#
# add_to_root_url_pattern(
#     (
#         #url(r'', include('social_auth.urls')),
#         # url(r'logged-in/', RedirectView.as_view(url='/object_filter/')),
#         # url(r'logged-in/', RedirectView.as_view(url='/socialprofile/')),
#         #url(r'logged-in/', RedirectView.as_view(url='/resource_bookmarks')),
#         #url(r'^accounts/', include('registration.backends.default.urls')),
#         #url(r'', RedirectView.as_view(url='/accounts/signin/')),
#         url(r'weibo/', RedirectView.as_view(url='/login/weibo/')),
#         #url(r'', include('userena.urls')),
#         url(r'^accounts/', include('userena.urls')),
#         url(r'^email_registration/', include('email_registration.urls')),
#
#
#         url(r'social/', include('social.apps.django_app.urls', namespace='social')),
#
#         #url(r'^accounts/profile', RedirectView.as_view(url='/yarr/unread/')),
#         #url(r'^accounts/profile/', include('userena.urls')),
#         # Will go to accounts/profile/ after login with social auth.
#         #url(r'^accounts/profile/', RedirectView.as_view(url='/webmanager/test_login/')),
#         url(r'^accounts/profile/', RedirectView.as_view(url='/webmanager/access_token/')),
#         url(r'^email-manager/', include('email_manager.urls', namespace='email_manager', app_name='email_manager')),
#     )
# )