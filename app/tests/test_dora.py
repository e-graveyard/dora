import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import dora as application
import pytest


@pytest.fixture
def client():
    application.dora.testing = True
    return application.dora.test_client()


def test_splash(client):
    response = client.get('/')
    assert response.status_code == 200


def test_invalid_endpoint(client):
    response = client.get('/an-invalid-endpoint')
    assert response.status_code == 404
