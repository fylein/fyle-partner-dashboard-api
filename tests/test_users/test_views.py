import json

import pytest
from django.urls import reverse
from apps.partner.models import PartnerOrg, User

from tests.fixture import fixture


@pytest.mark.django_db(databases=['default', 'cache_db'])
def test_profile_view(api_client, mocker, access_token):
    """"
    Test Get of My Profile
    """
    url = reverse('profile')

    api_client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(access_token))

    response = api_client.get(url)
    assert response.status_code == 200

    response = json.loads(response.content)
    assert response['data']['org']['id'] == 'orHVw3ikkCxJ'
    assert response['data']['user_id'] == 'usqywo0f3nBY'
