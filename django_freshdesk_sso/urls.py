from django.urls import path

from .views import sso

urlpatterns = [
    path('freshdesk/', sso, name='freshdesk_sso')
]
