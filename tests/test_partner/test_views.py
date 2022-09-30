import json

import pytest
from django.urls import reverse

from tests.helper import dict_compare_keys

from .fixture import fixture


@pytest.mark.django_db(databases=['default', 'cache_db'])
def test_partner_orgs_get_view(api_client, mocker, access_token):
    """"
    Test Get of Partner Orgs
    """
    url = reverse('partner_orgs')

    api_client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(access_token))

    response = api_client.get(url, {'primary_org_id': 'orHVw3ikkCxJ'})
    assert response.status_code == 200

    response = json.loads(response.content)
    assert dict_compare_keys(response, fixture['partner_orgs']) == [], 'partner_orgs GET diff in keys'

    response = api_client.get(url, {'primary_org_id': 'wrong_org_id'})
    assert response.status_code == 400

    response = json.loads(response.content)
    assert response['message'] != None


@pytest.mark.django_db(databases=['default', 'cache_db'])
def test_partner_orgs_put_view(api_client, mocker, access_token):
    """"
    Test Put of Partner Orgs
    """
    url = reverse('partner_orgs')

    api_client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(access_token))

    response = api_client.put(url)
    assert response.status_code == 200


@pytest.mark.django_db(databases=['default', 'cache_db'])
def test_new_partner_org_put_view(api_client, mocker, access_token):
    """"
    Test Put of New Partner Org
    """
    mocker.patch(
        'apps.partner.serializers.get_fyle_admin',
        return_value=fixture['my_profile_new_partner']
    )

    url = reverse('partner_orgs')

    api_client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(access_token))

    response = api_client.put(url)
    assert response.status_code == 200


@pytest.mark.django_db(databases=['default', 'cache_db'])
def test_orgs_get_view(api_client, mocker, access_token):
    """"
    Test Get of Partner Orgs
    """
    url = reverse('orgs')

    api_client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(access_token))

    response = api_client.get(url)
    assert response.status_code == 200

    response = json.loads(response.content)
    for org in response['data']:
      assert dict_compare_keys(org, fixture['orgs']) == [], 'orgs GET diff in keys'

@pytest.mark.django_db(databases=['default', 'cache_db'])
def test_ready_view(api_client, mocker, access_token):
    """"
    Test Get of Ready state
    """
    url = reverse('ready')
    response = api_client.get(url)
    assert response.status_code == 200
