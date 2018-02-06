from collections import OrderedDict

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

from .models import Page

# This view is called from FlatpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching flatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.
def flatpage(request, url):
    """
    Public interface to the flat page view.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or `flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """

    if not url.startswith('/'):
        url = '/' + url

    language = request.LANGUAGE_CODE
    #language_prefix = '/%s' % language

    #if url.startswith(language_prefix):
    #    url = url[len(language_prefix):]
    #kwargs = {
    #    '{0}__{1}'.format('url_%s' % language, 'exact'): url,
    #    '{0}__{1}'.format('site__id', 'exact'): settings.SITE_ID
    #}

    kwargs = {
        '{0}__{1}'.format('url_%s' % language, 'exact'): url,
        '{0}__{1}'.format('site__id', 'exact'): settings.SITE_ID
    }

    try:
        f = get_object_or_404(Page, **kwargs)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            f = get_object_or_404(Page, **kwargs)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise

    return render_flatpage(request, f)


@csrf_protect
def render_flatpage(request, page):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if page.login_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if page.template_name:
        page_template = loader.select_template((page.template_name, settings.CMS_PAGE_DEFAULT_TEMPLATE))
    else:
        page_template = loader.get_template(settings.CMS_PAGE_DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    page.h1_title = mark_safe(page.h1_title)

    section_list = page.sections.order_by('pagesectionthroughmodel')

    response = HttpResponse(page_template.render({
        'page': page,
        'section_list': section_list,
    }, request))

    try:
        from django.core.xheaders import populate_xheaders
        populate_xheaders(request, response, Page, f.id)
    except ImportError:
        pass
    return response

