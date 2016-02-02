from django.core.management.base import BaseCommand
from djangoautoconf.local_key_manager import get_local_key, ConfigurableAttributeGetter

from web_manage_tools.user_creator import create_admin


def create_default_admin():
    super_username = get_local_key("admin_account.admin_username", "webmanager.keys_default")
    super_password = get_local_key("admin_account.admin_password", "webmanager.keys_default")
    create_admin(super_username,
                 super_password, "r@j.cn")
    print "default admin created"


class Command(BaseCommand):
    args = ''
    help = 'Create command cache for environment where os.listdir is not working'

    def handle(self, *args, **options):
        create_default_admin()