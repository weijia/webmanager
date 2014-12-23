# Create your views here.
#from django.template import Context, loader
#from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import sys
import django
from django.contrib.auth import models as auth_models, authenticate, login
from cmd_utils import exec_django_cmd
from djangoautoconf.django_utils import retrieve_param
from management.commands.create_default_super_user import create_default_admin


def cmd(request):
    data = retrieve_param(request)
    import StringIO

    old_out = sys.stdout
    log_out = StringIO.StringIO()
    sys.stdout = log_out

    data_params = data["params"]
    exec_django_cmd(data_params)

    result = log_out.getvalue()
    sys.stdout = old_out
    return HttpResponse(result.replace("\n", "<br/>"))


def version(request):
    #from obj_sys.baidu_mail import EmailBackend
    return HttpResponse(django.VERSION)


def handle_create_admin_req(request):
    create_default_admin()
    return HttpResponse('Done<script>window.href="/"</script>')


def login_and_go_home(request):
    data = retrieve_param(request)
    target = data.get("target", "/obj_sys/homepage/")
    if not request.user.is_authenticated():
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect(target)