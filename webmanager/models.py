from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel

from djangoautoconf.model_utils.len_definitions import TEXT_LENGTH_4096

try:
    from userena.models import UserenaBaseProfile


    class MyProfile(UserenaBaseProfile):
        user = models.OneToOneField(User,
                                    unique=True,
                                    verbose_name=_('user'),
                                    related_name='my_profile')
        favourite_snack = models.CharField(_('favourite snack'),
                                           max_length=5)
except ImportError:
    pass


class DebugRequestParam(TimeStampedModel):
    request_json = models.CharField(max_length=TEXT_LENGTH_4096)
