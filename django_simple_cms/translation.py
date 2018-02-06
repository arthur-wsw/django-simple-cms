from modeltranslation.translator import register, TranslationOptions

from .models import Page, HtmlSectionContent, TextSectionContent, ImageSectionContent


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('name', 'h1_title', 'seo_title', 'seo_description', 'seo_og_image_alt', 'url',)


@register(HtmlSectionContent)
class HtmlSectionContentOptions(TranslationOptions):
    fields = ('html',)


@register(TextSectionContent)
class TextSectionContentOptions(TranslationOptions):
    fields = ('text',)


@register(ImageSectionContent)
class ImageSectionContentOptions(TranslationOptions):
    fields = ('alt_text',)
