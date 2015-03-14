from django.contrib.auth.models import Permission
from djangoautoconf.auto_conf_admin_utils import register_all
from provider.oauth2.models import RefreshToken, AccessToken

__author__ = 'weijia'

register_all([Permission])


# try:
#     from provider.oauth2.backends import AccessTokenBackend
#     #register_all([AccessToken, RefreshToken])
# except ImportError:
#     pass