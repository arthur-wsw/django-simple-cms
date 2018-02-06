from django import forms
from django.conf import settings
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _

from .models import Page


class PageForm(forms.ModelForm):
    REQUIRED_MIDDLEWARE = 'django.middleware.common.CommonMiddleware'

    def clean_url_value(self, url_key):
        url = self.cleaned_data.get(url_key, None)

        if url in EMPTY_VALUES:
            return

        # check leading slash
        if not url.startswith('/'):
            raise forms.ValidationError(_(u"URL '%(url)s' is missing a leading slash.") % {'url': url})

        # check trailing slash
        if settings.APPEND_SLASH and self.REQUIRED_MIDDLEWARE in settings.MIDDLEWARE and not url.endswith('/'):
            raise forms.ValidationError(_(u"URL '%(url)s' is missing a trailing slash.") % {'url': url})

        # check URL uniqueness
        site = self.cleaned_data.get('site', None)

        kwargs = {
            '{0}__{1}'.format(url_key, 'exact'): url,
        }
        same_url = Page.objects.filter(**kwargs)

        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        if site is None:
            raise forms.ValidationError(_(u'No sites selected!'))

        if same_url.filter(site=site).exists():
            raise forms.ValidationError(_(u"Flatpage with URL '%(url)s' already exists \
                                          for site %(site)s.") % {'url': url, 'site': site})
        return url

    def clean(self):
        for language in dict(settings.LANGUAGES).keys():
            url_key = 'url_%s' % language
            self.clean_url_value(url_key)
        return super(PageForm, self).clean()

    class Meta:
        model = Page
        exclude = ()
