# Create your views here.
#from django.template import Context, loader
#from django.contrib.auth.models import User
#from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import sys
import django
from django.contrib.auth import authenticate, login
from cmd_utils import exec_django_cmd
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.req_with_auth import complex_login
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
        complex_login(request)
    return HttpResponseRedirect(target)


def test_login(request):
    res = ""
    if not request.user.is_authenticated():
        res = "Complex login called"
        complex_login(request)
    if request.user.is_authenticated():
        res += "Login OK: %s" % request.user.username
    return HttpResponse(res)


def weibo_login(request):
    return HttpResponse('<a href="/login/weibo/"><img src="http://www.sinaimg.cn/blog/developer/wiki/48.png"/></a>')