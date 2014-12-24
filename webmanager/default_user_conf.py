try:
    from keys.template_keys.admin_pass import default_admin_password, default_admin_user
except ImportError:
    from external_git.webmanager.webmanager.management.commands.keys_default.admin_pass import default_admin_password, default_admin_user
    
    
def get_default_username_and_pass():
    return default_admin_user, default_admin_password