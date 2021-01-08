====================
Django Freshdesk SSO
====================
.. image:: https://badge.fury.io/py/django-freshdesk-sso.svg
    :target: https://badge.fury.io/py/django-freshdesk-sso

Django Freshdesk SSO enables SSO for freshdesk from your django application.

This package replaces the stale and out of date `django-freshdesk <https://pypi.org/project/django-freshdesk/>`_ package.

Quick start
-----------

1. Add "freshdesk_sso" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'freshdesk_sso',
    ]

2. Include the freshdesk SSO URLconf in your project urls.py like this::

    path('accounts/login/sso/', include('freshdesk_sso.urls')),


3. Add the required environment variables to your settings.py file::

    FRESHDESK_URL = 'http://yourcompany.freshdesk.com/'
    FRESHDESK_SECRET_KEY = 'YOUR_SECRET_GOES_HERE'

