# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Page,
	Section,
	PageSectionThroughModel,
	SectionContent,
	HtmlSectionContent,
	TextSectionContent,
	ImageSectionContent,
	LinkSectionContent,
)


class PageCreateView(CreateView):

    model = Page


class PageDeleteView(DeleteView):

    model = Page


class PageDetailView(DetailView):

    model = Page


class PageUpdateView(UpdateView):

    model = Page


class PageListView(ListView):

    model = Page


class SectionCreateView(CreateView):

    model = Section


class SectionDeleteView(DeleteView):

    model = Section


class SectionDetailView(DetailView):

    model = Section


class SectionUpdateView(UpdateView):

    model = Section


class SectionListView(ListView):

    model = Section


class PageSectionThroughModelCreateView(CreateView):

    model = PageSectionThroughModel


class PageSectionThroughModelDeleteView(DeleteView):

    model = PageSectionThroughModel


class PageSectionThroughModelDetailView(DetailView):

    model = PageSectionThroughModel


class PageSectionThroughModelUpdateView(UpdateView):

    model = PageSectionThroughModel


class PageSectionThroughModelListView(ListView):

    model = PageSectionThroughModel


class SectionContentCreateView(CreateView):

    model = SectionContent


class SectionContentDeleteView(DeleteView):

    model = SectionContent


class SectionContentDetailView(DetailView):

    model = SectionContent


class SectionContentUpdateView(UpdateView):

    model = SectionContent


class SectionContentListView(ListView):

    model = SectionContent


class HtmlSectionContentCreateView(CreateView):

    model = HtmlSectionContent


class HtmlSectionContentDeleteView(DeleteView):

    model = HtmlSectionContent


class HtmlSectionContentDetailView(DetailView):

    model = HtmlSectionContent


class HtmlSectionContentUpdateView(UpdateView):

    model = HtmlSectionContent


class HtmlSectionContentListView(ListView):

    model = HtmlSectionContent


class TextSectionContentCreateView(CreateView):

    model = TextSectionContent


class TextSectionContentDeleteView(DeleteView):

    model = TextSectionContent


class TextSectionContentDetailView(DetailView):

    model = TextSectionContent


class TextSectionContentUpdateView(UpdateView):

    model = TextSectionContent


class TextSectionContentListView(ListView):

    model = TextSectionContent


class ImageSectionContentCreateView(CreateView):

    model = ImageSectionContent


class ImageSectionContentDeleteView(DeleteView):

    model = ImageSectionContent


class ImageSectionContentDetailView(DetailView):

    model = ImageSectionContent


class ImageSectionContentUpdateView(UpdateView):

    model = ImageSectionContent


class ImageSectionContentListView(ListView):

    model = ImageSectionContent


class LinkSectionContentCreateView(CreateView):

    model = LinkSectionContent


class LinkSectionContentDeleteView(DeleteView):

    model = LinkSectionContent


class LinkSectionContentDetailView(DetailView):

    model = LinkSectionContent


class LinkSectionContentUpdateView(UpdateView):

    model = LinkSectionContent


class LinkSectionContentListView(ListView):

    model = LinkSectionContent

