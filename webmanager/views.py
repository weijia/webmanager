# Create your views here.
#from django.template import Context, loader
#from django.contrib.auth.models import User
#from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import sys
import django
from django.contrib.auth import models as auth_models, authenticate, login
from django.utils import timezone
from provider.oauth2.backends import AccessTokenBackend
from provider.oauth2.models import AccessToken
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


def login_from_oauth2(request):
    data = retrieve_param(request)
    target = data.get("target", "/admin")
    if "access_token" in data:
        access_tokens = AccessToken.objects.filter(token=data["access_token"], expires__gt=timezone.now())
        if access_tokens.exists():
            user_access_token = access_tokens[0]
            user_access_token.expires = timezone.now()
            user_access_token.save()
            user_instance = user_access_token.user  # User.objects.get(username=user_access_token.user)
            user_instance.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user_instance)
    return HttpResponseRedirect(target)