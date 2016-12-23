from djangoautoconf.django_utils import retrieve_param
from django.utils import timezone
from provider.oauth2.backends import AccessTokenBackend
from provider.oauth2.models import AccessToken
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login

from djangoautoconf.req_with_auth import login_by_django_user


def login_from_oauth2(request):
    data = retrieve_param(request)
    target = data.get("target", "/admin")
    if "access_token" in data:
        access_tokens = AccessToken.objects.filter(token=data["access_token"], expires__gt=timezone.now())
        if access_tokens.exists():
            user_access_token = access_tokens[0]
            user_access_token.expires = timezone.now()
            user_access_token.save()
            django_user_instance = user_access_token.user
            login_by_django_user(django_user_instance, request)
    return HttpResponseRedirect(target)
