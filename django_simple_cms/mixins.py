from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured

from .models import Page


class PageMixin(object):
    """
    Retrieves the FlatPage object for the specified url, and includes it in the
    context.
    If no url is specified, request.path is used.
    """
    page_slug = None

    def get_page_slug(self):
        if not self.page_slug:
            raise ImproperlyConfigured("No slug to find SEO page. Provide a page_slug.")
        return self.page_slug

    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)
        seo_page, created = Page.objects.get_or_create(
            slug=self.get_page_slug(),
            site=get_current_site(self.request),
            defaults={

            },
        )
        context.update({
            'seo_page': seo_page,
            'seo_title': self.get_seo_title(seo_page),
            'seo_no_index': self.get_seo_no_index(seo_page),
            'seo_description': self.get_seo_description(seo_page),
            'seo_og_type': self.get_seo_og_type(seo_page),
            'seo_og_url': self.get_seo_og_url(seo_page),
            'seo_og_image': self.get_seo_og_image(seo_page),
            'seo_og_description': self.get_seo_og_description(seo_page),
            'seo_og_sitename': self.get_seo_og_sitename(seo_page),
            'seo_twitter_card': self.get_seo_twitter_card(seo_page),
            'seo_twitter_site': self.get_seo_twitter_site(seo_page),
            'seo_twitter_title': self.get_seo_twitter_title(seo_page),
            'seo_twitter_description': self.get_seo_twitter_description(seo_page),
            'seo_twitter_image': self.get_seo_twitter_image(seo_page),
            'seo_twitter_image_alt': self.get_seo_twitter_image_alt(seo_page),
        })
        return context

    def get_seo_no_index(self, seo_page):
        if seo_page:
            return seo_page.no_index
        return None

    def get_seo_title(self, seo_page):
        if seo_page:
            return seo_page.seo_title
        return None

    def get_seo_description(self, seo_page):
        if seo_page:
            return seo_page.seo_description
        return None

    def get_seo_og_type(self, seo_page):
        return settings.SEO_OG_TYPE

    def get_seo_og_url(self, seo_page):
        site = get_current_site(self.request)
        return '%(protocol)s://%(prepend_www)s%(domain)s%(path)s' % {
            'protocol': settings.SEO_PROTOCOL,
            'prepend_www': 'www.' if settings.SEO_PREPEND_WWW else '',
            'domain': site.domain,
            'path': self.request.path,
        }

    def get_seo_og_image(self, seo_page):
        if seo_page:
            if seo_page.seo_og_image:
                return seo_page.seo_og_image.url
        return settings.SEO_OG_IMAGE_URL

    def get_seo_og_description(self, seo_page):
        if seo_page:
            return seo_page.seo_description
        return None

    def get_seo_og_sitename(self, seo_page):
        return settings.SEO_OG_SITENAME

    def get_seo_twitter_card(self, seo_page):
        return settings.SEO_TWITTER_CARD

    def get_seo_twitter_site(self, seo_page):
        return settings.SEO_TWITTER_SITE

    def get_seo_twitter_title(self, seo_page):
        if seo_page:
            return seo_page.seo_title
        return None

    def get_seo_twitter_description(self, seo_page):
        if seo_page:
            return seo_page.seo_description
        return None

    def get_seo_twitter_image(self, seo_page):
        if seo_page:
            if seo_page.seo_og_image:
                return seo_page.seo_og_image.url
        return settings.SEO_OG_IMAGE_URL

    def get_seo_twitter_image_alt(self, seo_page):
        if seo_page:
            return seo_page.seo_og_image_alt
        return None
