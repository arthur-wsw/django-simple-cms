=====
Usage
=====

To use Django Simple CMS in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_simple_cms.apps.DjangoSimpleCmsConfig',
        ...
    )

Add Django Simple CMS's URL patterns:

.. code-block:: python

    from django_simple_cms import urls as django_simple_cms_urls


    urlpatterns = [
        ...
        url(r'^', include(django_simple_cms_urls)),
        ...
    ]
