from django.urls import path

from .views import PartnerView

urlpatterns = [
    path('', PartnerView.as_view(), name='partner')
]
