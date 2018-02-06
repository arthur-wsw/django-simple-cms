from builtins import str as text

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin
from ordered_model.admin import OrderedTabularInline

from .forms import PageForm
from .models import Page, Section, PageSectionThroughModel, SectionContent, HtmlSectionContent, TextSectionContent, ImageSectionContent


class PageSectionThroughModelInline(OrderedTabularInline):
    model = PageSectionThroughModel
    fields = ('section', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    extra = 1
    ordering = ('order',)


@admin.register(Page)
class PageAdmin(MPTTModelAdmin, TranslationAdmin):
    form = PageForm
    mptt_level_indent = 0

    fieldsets = (
        (None, {
            'fields': ('parent', 'slug', 'name', 'url', 'site', 'weight')
        }),
        (_('SEO'), {
            'classes': ('collapse',),
            'fields': ('h1_title', 'seo_title', 'seo_description', 'seo_og_image', 'seo_og_image_alt', 'no_index',)
        }),
        (_(u'Permission'), {
            'classes': ('collapse',),
            'fields': ('login_required',)
        })
    )
    list_display = ('indented_title', 'url', 'parent', 'weight')
    list_filter = ('site', 'login_required')
    list_editable = ['parent', 'weight']
    search_fields = ('url', 'title')
    readonly_fields = ('created', 'modified')
    inlines = (PageSectionThroughModelInline, )

    class Media:
        js = ('js/flatpages_i18n/jquery.js', )
        css = {
            'all': ('css/flatpages_i18n/admin.css', )
        }

    def __init__(self, *args, **kwargs):
        super(TranslationAdmin, self).__init__(*args, **kwargs)
        self._patch_list_editable()

    def get_urls(self):
        urls = super(PageAdmin, self).get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls

    def indented_title(self, obj):
        level = getattr(obj, obj._mptt_meta.level_attr)

        if level is 0:
            return obj

        level_indicator = ''.join(['-' for i in range(level)])
        return u'%s %s' % (level_indicator, text(obj))



class SectionContentInline(admin.TabularInline):
    model = SectionContent
    fields = ('slug', )
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = (SectionContentInline, )



@admin.register(SectionContent)
class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_page', 'section', 'get_section_multipage', 'slug',)

    def get_page(self, obj):
        pages = obj.section.page_set.all()
        count = pages.count()
        if count == 1:
            return pages.first()
        else:
            return '%s - %s' % (count, pages)
    get_page.short_description = 'Pages'
    #get_page.admin_order_field = 'book__author'

    def get_section_multipage(self, obj):
        return obj.section.multipage
    get_section_multipage.short_description = _('section multipage')
    get_section_multipage.boolean = True
    get_section_multipage.admin_order_field = 'section__multipag'

@admin.register(HtmlSectionContent)
class HtmlSectionContentAdmin(TranslationAdmin, SectionContentAdmin):
    pass



@admin.register(TextSectionContent)
class TextSectionContentAdmin(TranslationAdmin, SectionContentAdmin):
    pass


@admin.register(ImageSectionContent)
class ImageSectionContentAdmin(TranslationAdmin, SectionContentAdmin):
    pass
