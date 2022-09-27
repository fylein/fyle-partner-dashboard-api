import os
from unittest import mock
from datetime import datetime,timezone
import pytest
from fyle_rest_auth.models import User,AuthToken
from rest_framework.test import APIClient
from fyle.platform import Platform
from fyle_partner_dashboard_api import settings

from tests.fixture import fixture


def pytest_configure():
    os.system('sh ./tests/sql_fixtures/reset_db_fixtures/reset_db.sh')

@pytest.fixture
def api_client():
    return APIClient()
