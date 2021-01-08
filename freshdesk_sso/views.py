import hmac
from hashlib import md5
from time import time

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseRedirect
from django.utils.http import urlencode
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def sso(request):
    if not hasattr(settings, 'FRESHDESK_URL'):
        raise ImproperlyConfigured('Set the FRESHDESK_URL settings variable')
    if not hasattr(settings, 'FRESHDESK_SECRET_KEY'):
        raise ImproperlyConfigured('Set the FRESHDESK_SECRET_KEY settings variable')

    if not request.user:
        raise Http404()

    full_name = request.user.get_full_name() or request.user.get_username()
    email = request.user.email
    utctime = int(time())

    generated_hash = hmac.new(
        settings.FRESHDESK_SECRET_KEY.encode(),
        f'{full_name}{settings.FRESHDESK_SECRET_KEY}{email}{utctime}'.encode(),
        md5
    ).hexdigest()

    params = urlencode({
        'name': full_name,
        'email': email,
        'timestamp': utctime,
        'hash': generated_hash
    })

    return HttpResponseRedirect(f'{settings.FRESHDESK_URL}login/sso?{params}')
