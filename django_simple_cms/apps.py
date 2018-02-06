from django.apps import AppConfig as CoreAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(CoreAppConfig):
    name = 'django_simple_cms'
    verbose_name = _("CMS")
