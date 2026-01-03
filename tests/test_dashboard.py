def test_dashboard_unauthorized(client):
    response = client.get("/dashboard")
    assert client.status_code == 401
    