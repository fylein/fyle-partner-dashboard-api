from django.urls import path

from .views import PartnerOrgView, OrgsView

urlpatterns = [
    path('', PartnerOrgView.as_view(), name='partner_orgs'),
    path('orgs/', OrgsView.as_view(), name='orgs')
]
