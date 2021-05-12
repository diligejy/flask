from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert '{"text":"Hello, World"}' in str(response.data)
    assert '{"count":0}' in str(response.data)

    response = client.get('/')
    assert response.status_code == 200
    assert '{"count":1}' in str(response.data)

    # GET
    # HTTP Status 200
    # Hello, world
    assert 1 + 1 == 2
