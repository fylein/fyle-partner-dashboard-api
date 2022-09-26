"""
Partner Serializers
"""
from rest_framework import serializers

from .models import PartnerOrg


class PartnerOrgSerializer(serializers.ModelSerializer):
    """
    Partner Org serializer
    """
    class Meta:
        model = PartnerOrg
        fields = '__all__'
