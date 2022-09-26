from django.contrib.auth import get_user_model
from django.core.cache import cache

from rest_framework import generics, status
from rest_framework.response import Response

from fyle_rest_auth.helpers import get_fyle_admin

from apps.partner.models import PartnerOrg

from .helpers import get_cluster_domain
from .serializers import PartnerOrgSerializer


User = get_user_model()


class PartnerView(generics.GenericAPIView):
    def post(self, request):
        """
        Create a Partner Org
        """
        auth = request.META.get('HTTP_AUTHORIZATION')
        access_token = auth.split(' ')[1]

        user_profile = get_fyle_admin(access_token, None)

        primary_org_name = user_profile['data']['org']['name']
        primary_org_id = user_profile['data']['org']['id']

        partner_org = PartnerOrg.objects.filter(primary_org_id=primary_org_id).first()

        if partner_org:
            partner_org.user.add(User.objects.get(user_id=request.user))
            cache.delete(str(partner_org.id))
        else:
            cluster_domain = get_cluster_domain(access_token)

            partner_org = PartnerOrg.objects.create(
                name=primary_org_name, primary_org_id=primary_org_id, cluster_domain=cluster_domain
            )

            partner_org.user.add(User.objects.get(user_id=request.user))

        return Response(
            data=PartnerOrgSerializer(partner_org).data,
            status=status.HTTP_200_OK
        )

    def get(self, request):
        """
        Get workspace
        """
        user = User.objects.get(user_id=request.user)
        primary_org_id = request.query_params.get('primary_org_id')
        workspace = PartnerOrg.objects.filter(user__in=[user], primary_org_id=primary_org_id).all()

        return Response(
            data=PartnerOrgSerializer(workspace, many=True).data,
            status=status.HTTP_200_OK
        )
