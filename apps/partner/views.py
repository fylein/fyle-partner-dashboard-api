from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response

from apps.partner.models import PartnerOrg

from .serializers import PartnerOrgSerializer


User = get_user_model()


class PartnerOrgView(generics.RetrieveUpdateAPIView):
    serializer_class = PartnerOrgSerializer

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(user_id=self.request.user)
            primary_org_id = self.request.query_params.get('primary_org_id')
            parnter_org = PartnerOrg.objects.get(user__in=[user], primary_org_id=primary_org_id)

            return Response(
                data=PartnerOrgSerializer(parnter_org).data,
                status=status.HTTP_200_OK
            )
        except PartnerOrg.DoesNotExist:
            return Response(
                data={'message': 'Partner Org Not Found'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get_object(self):
        return self.get(self)
