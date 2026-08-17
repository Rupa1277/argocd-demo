from app import app

def test_hello_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_hello_content():
    client = app.test_client()
    response = client.get("/")
    assert b"Version" in response.data