from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from forms_captcha import CaptchaTestForm

__author__ = 'weijia'


def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()
    csrf_token = csrf(request)["csrf_token"]

    return render_to_response('webmanager/captcha.html',locals())