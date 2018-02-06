=============================
Django Simple CMS
=============================

.. image:: https://badge.fury.io/py/django-simple-cms.svg
    :target: https://badge.fury.io/py/django-simple-cms

.. image:: https://travis-ci.org/arthur-wsw/django-simple-cms.svg?branch=master
    :target: https://travis-ci.org/arthur-wsw/django-simple-cms

.. image:: https://codecov.io/gh/arthur-wsw/django-simple-cms/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/arthur-wsw/django-simple-cms

Django CMS by WallStreetWeb.

Documentation
-------------

The full documentation is at https://django-simple-cms.readthedocs.io.

Quickstart
----------

Install Django Simple CMS::

    pip install django-simple-cms

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
