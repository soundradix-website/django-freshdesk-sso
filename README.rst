====================
Django Freshdesk SSO
====================

Django Freshdesk SSO enables SSO for freshdesk from your django application.

Quick start
-----------

1. Add "freshdesk_sso" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'freshdesk_sso',
    ]

2. Include the freshdesk SSO URLconf in your project urls.py like this::

    path('accounts/login/sso/', include('freshdesk_sso.urls')),

