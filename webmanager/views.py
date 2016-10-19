# Create your views here.
#from django.template import Context, loader
#from django.contrib.auth.models import User
#from django.contrib.auth.backends import ModelBackend
import json
import datetime

from compat.json_response import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import sys
import django
from django.contrib.auth import authenticate, login
from django.utils.timezone import utc
from django.views.decorators.csrf import csrf_exempt
from provider.oauth2.models import AccessToken, Client
from provider.oauth2.views import AccessTokenView
from cmd_utils import exec_django_cmd
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.management.commands.create_default_super_user import create_default_admin
from djangoautoconf.req_with_auth import complex_login, RequestWithAuth, assert_username_password


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
        complex_login(request)
    return HttpResponseRedirect(target)


def test_login(request):
    res = ""
    if not request.user.is_authenticated():
        res = "Complex login called"
        complex_login(request)
    if request.user.is_authenticated():
        res += "Login OK: %s" % request.user.username
        res += ", %s" % get_access_token(request)
    return HttpResponse(res)


def get_latest_access_token(not_exp_time, user):
    access_token, is_created = AccessToken.objects.get_or_create(
        user=user,
        client=Client.objects.get(pk=1),
        expires__gt=not_exp_time
    )
    return access_token


def get_access_token(user):
    now_with_tz = datetime.datetime.utcnow().replace(tzinfo=utc)
    not_exp_time = now_with_tz - datetime.timedelta(days=1)
    try:
        access_token = get_latest_access_token(not_exp_time, user)
    except:
        c, is_created = Client.objects.get_or_create(pk=1, client_type=1)
        AccessToken.objects.filter(user=user,
                                   client=c).delete()
        access_token = get_latest_access_token(not_exp_time, user)

    access_token.expires = now_with_tz + datetime.timedelta(days=5)
    access_token.save()
    return access_token


@csrf_exempt
def handle_get_access_token_req(request):
    try:
        assert_username_password(request)
        return JsonResponse(get_access_token_response_dict(request.user))
    except:
        return HttpResponse('Unauthorized', status=401)


def get_access_token_response_dict(user):
    res = {"username": user.username, "user_id": user.id}
    access_token = get_access_token(user)
    res["access_token"] = access_token.token
    return res


@csrf_exempt
def handle_get_access_token_req_with_session(request):
    res = {}
    req_with_auth = RequestWithAuth(request)
    if req_with_auth.is_authenticated() and request.user.is_authenticated():
        res["username"] = request.user.username
        res["user_id"] = request.user.id
        access_token = get_access_token(request)
        res["access_token"] = access_token.token
        return JsonResponse(res)
    return HttpResponse('Unauthorized', status=401)


def weibo_login(request):
    return HttpResponse('<a href="/login/weibo/"><img src="http://www.sinaimg.cn/blog/developer/wiki/48.png"/></a>')


def raise_error(request):
    raise
