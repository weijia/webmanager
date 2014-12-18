from django.core.management.base import BaseCommand, CommandError
import django.core.management as core_management
from web_manage_tools.user_creator import create_admin


try:
    from keys.admin_pass import default_admin_password, default_admin_user
except ImportError:
    from keys_template.admin_pass import default_admin_password, default_admin_user


def create_default_admin():
    create_admin(default_admin_user, default_admin_password, "r@j.cn")
    print "default admin created"


class Command(BaseCommand):
    args = ''
    help = 'Create command cache for environment where os.listdir is not working'

    def handle(self, *args, **options):
        create_default_admin()