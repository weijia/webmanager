from django.core.management.base import BaseCommand
from djangoautoconf.local_key_manager import get_local_key, ConfigurableAttributeGetter

from web_manage_tools.user_creator import create_admin


# try:
#     from keys.local_keys.admin_pass import default_admin_password, default_admin_user
# except ImportError:
#     from keys_default.admin_pass import default_admin_password, default_admin_user


def create_default_admin():
    getter = ConfigurableAttributeGetter("admin_account", "webmanager.keys_default")
    super_username = getter.get_attr("admin_username")
    super_password = getter.get_attr("admin_password")
    create_admin(super_username,
                 super_password, "r@j.cn")
    print "default admin created"


class Command(BaseCommand):
    args = ''
    help = 'Create command cache for environment where os.listdir is not working'

    def handle(self, *args, **options):
        create_default_admin()