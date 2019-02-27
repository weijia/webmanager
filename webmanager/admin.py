from django.contrib.auth.models import Permission
from djangoautoconf.auto_conf_admin_tools.admin_register import AdminRegister
# from djangoautoconf.auto_conf_admin_utils import register_all
from webmanager.models import DebugRequestParam

__author__ = 'weijia'

# register_all([Permission])

r = AdminRegister()
r.register(Permission)
r.register(DebugRequestParam)
