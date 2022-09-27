from django.urls import path

from .views import PartnerOrgView

urlpatterns = [
    path('', PartnerOrgView.as_view(), name='partner_orgs')
]
