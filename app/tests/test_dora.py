import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import dora

def test_splash():
    dora.application.testing = True
    client = dora.application.test_client()

    response = client.get('/')
    assert response.status_code == 200
