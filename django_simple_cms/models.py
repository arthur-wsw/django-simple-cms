from django.contrib.sites.models import Site
from django.db import models
from django.db import models
from django.utils import translation
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.managers import InheritanceManager
from model_utils.models import TimeStampedModel
from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey
from ordered_model.models import OrderedModel


class Page(TimeStampedModel, MPTTModel):
    WEIGHT = [(i, i) for i in range(-10, 10)]
    site = models.ForeignKey(Site, verbose_name=_('site'), on_delete=models.CASCADE)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, help_text=_('Identifiant unique de la page'))
    url = models.CharField(_('URL'), max_length=100, db_index=True, help_text=_("Exemple: '/about/contact/'. Assurez-vous que l'url commence et termine par des /."))

    parent = TreeForeignKey('self', verbose_name=_('page parente'), related_name='children', null=True, blank=True, on_delete=models.SET_NULL)
    weight = models.IntegerField(_('poids de la page'), null=True, blank=True, default=0, choices=WEIGHT, help_text=_("Utilisez cette valeur pour modifier l'ordre des page"))
    login_required = models.BooleanField(_('inscription requise ?'), default=False, help_text=_('Si cette case est cochée, seuls les utilisateurs connectés pourront voir la page.'))

    name = models.CharField(_("nom"), max_length=90, help_text=_("Le nom affiché dans le fil d'ariane"))
    h1_title = models.TextField(_('titre H1'), max_length=200)
    seo_title = models.CharField(_('meta title'), max_length=90, blank=True, null=True, help_text=_('Titre SEO pour Google, Facebook et Twitter'))
    seo_description = models.CharField(_('meta description'), max_length=400, blank=True, null=True, help_text=_('Description SEO pour Google, Facebook et Twitter'))
    seo_og_image = models.ImageField(_('OpenGraph image'), blank=True, null=True, help_text=_('Image pour le partage Facebook et Twitter'))
    seo_og_image_alt = models.CharField(_('OpenGraph image alt'), max_length=420, blank=True, null=True, help_text=_("Description de l'image utilisée pour le partage Facebook et Twitter"))
    no_index = models.BooleanField(_('ne pas référencer la page ?'), default=False, help_text=_("Supprime la page du référencement Google"))

    template_name = models.CharField(_('nom du template'), max_length=70, blank=True, help_text=_("Par défault définie à 'pages/flatpages/{{page.slug}}.htlm' ou 'pages/flatpages/base.htlm'"))
    sections = models.ManyToManyField('django_simple_cms.Section', through='PageSectionThroughModel')
    is_home = models.BooleanField(editable=False, db_index=True, default=False)

    def get_absolute_url(self):
        return self.url

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['weight']

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('weight', 'created')


class Section(TimeStampedModel):
    name = models.CharField(_('nom'), max_length=255, blank=True, null=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, help_text=_('Identifiant unique de la section'))
    template_name = models.CharField(_('nom du template'), max_length=70, blank=True, help_text=_("Par défault définie à 'pages/flatpages/{{page.slug}}.htlm' ou 'pages/flatpages/base.htlm'"))
    multipage = models.BooleanField(_('multi page'), default=False, help_text=_('Cette section apparait-elle sur plusieurs pages?'))

    def get_section_content(self, content_slug):
        return self.contents.get_subclass(slug=content_slug)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')


class PageSectionThroughModel(TimeStampedModel, OrderedModel):
    page = models.ForeignKey('django_simple_cms.Page', on_delete=models.CASCADE)
    section = models.ForeignKey('django_simple_cms.Section', on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')


class SectionContent(TimeStampedModel):
    slug = models.SlugField(_('slug'), max_length=255, help_text=_('Identifiant du contenu dans la section'))
    section = models.ForeignKey('django_simple_cms.Section', verbose_name=_('section'), related_name='contents',
                                on_delete=models.CASCADE)

    objects = InheritanceManager()

    class Meta:
        verbose_name = _('section content')
        verbose_name_plural = _('section contents')
        unique_together = ('slug', 'section')


class HtmlSectionContent(SectionContent):
    html = models.TextField(_('html'))


class TextSectionContent(SectionContent):
    text = models.TextField(_('texte'))


class ImageSectionContent(SectionContent):
    image = models.ImageField(_('image'))
    alt_text = models.CharField(_('balise alt'), max_length=255, blank=True, null=True)


class LinkSectionContent(SectionContent):
    pass


class IconSectionContent(SectionContent):
    pass



