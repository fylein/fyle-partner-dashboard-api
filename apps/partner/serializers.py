"""
Partner Serializers
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.cache import cache

from fyle_rest_auth.helpers import get_fyle_admin

from .models import PartnerOrg
from .helpers import get_cluster_domain


User = get_user_model()


class PartnerOrgSerializer(serializers.ModelSerializer):
    """
    Partner Org serializer
    """
    class Meta:
        model = PartnerOrg
        fields = '__all__'
        read_only_fields = [
         'name', 'primary_org_id', 'cluster_domain', 'user'
        ]

    def update(self, instance, validated):
        auth = self.context['request'].META.get('HTTP_AUTHORIZATION')
        access_token = auth.split(' ')[1]

        user_profile = get_fyle_admin(access_token, None)

        primary_org_name = user_profile['data']['org']['name']
        primary_org_id = user_profile['data']['org']['id']

        partner_org = PartnerOrg.objects.filter(primary_org_id=primary_org_id).first()

        if partner_org:
            partner_org.user.add(User.objects.get(user_id=self.context['request'].user))
            cache.delete(str(partner_org.id))
        else:
            cluster_domain = get_cluster_domain(access_token)
            currency = user_profile['data']['org']['currency']

            partner_org = PartnerOrg.objects.create(
                name=primary_org_name, primary_org_id=primary_org_id, cluster_domain=cluster_domain, currency=currency
            )

            partner_org.user.add(User.objects.get(user_id=self.context['request'].user))

        return partner_org
