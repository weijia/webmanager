__author__ = 'weijia'


from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm, SignupFormOnlyEmail
from captcha.fields import CaptchaField


class SignupFormWithCaptcha(SignupFormOnlyEmail):
    captcha = CaptchaField()


class CaptchaSignupFormWithBootstrap(SignupFormWithCaptcha):
    def __init__(self, *args, **kwargs):
        super(CaptchaSignupFormWithBootstrap, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})