from conftest import client



def test(client):
    response = client.get('/')
    assert response.status_code == 200

